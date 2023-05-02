import kotlinx.coroutines.*
import kotlinx.coroutines.channels.Channel
import kotlinx.coroutines.channels.SendChannel
import kotlinx.coroutines.channels.actor
import java.io.File
import java.util.concurrent.atomic.AtomicInteger
import kotlin.system.*

sealed class CounterMessage {
    object Increment : CounterMessage()
    class GetValue(val response: CompletableDeferred<Int>) : CounterMessage()
}

fun CoroutineScope.counterActor(fileChannel: SendChannel<Int>) = actor<CounterMessage> {
    var counter = 0

    for (msg in channel) {
        when (msg) {
            is CounterMessage.Increment -> {
                counter++
                if (counter % 500 == 0) {
                    fileChannel.send(counter)
                }
            }
            is CounterMessage.GetValue -> msg.response.complete(counter)
        }
    }
}

fun CoroutineScope.fileActor() = actor<Int> {
    for (msg in channel) {
        File("output.txt").appendText("${msg}\n")
    }
}

suspend fun CoroutineScope.massiveRun(action: suspend () -> Unit) {
    val n = 100
    val k = 1000
    val time = measureTimeMillis {
        val jobs = List(n)
        {
            launch { repeat(k) { action() } }
        }
        jobs.forEach { it.join() }
    }
    println("S-au efectuat ${n * k} operatii in $time ms")
}

val mtContext = newFixedThreadPoolContext(2, "mtPool")

fun main() = runBlocking<Unit> {
    val scope = CoroutineScope(mtContext)

    val fileChannel = scope.fileActor()
    val counterChannel = scope.counterActor(fileChannel)

    scope.massiveRun {
        counterChannel.send(CounterMessage.Increment)
    }

    val response = CompletableDeferred<Int>()
    counterChannel.send(CounterMessage.GetValue(response))
    println("Contor = ${response.await()}")

    counterChannel.close()
    fileChannel.close()

}