import kotlinx.coroutines.*
import kotlinx.coroutines.channels.Channel
import kotlinx.coroutines.sync.Mutex
import kotlinx.coroutines.sync.withLock
import java.io.File
import java.util.concurrent.atomic.AtomicInteger
import kotlin.system.*

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
var counter = AtomicInteger()

fun main() = runBlocking {
    val scope = CoroutineScope(mtContext)

    val fileWriter = Channel<Int>(capacity = Channel.UNLIMITED).also { channel ->
        scope.launch {
            for (msg in channel) {
                File("output.txt").appendText("${msg}\n")
            }
        }
    }

    scope.massiveRun {
        val value = counter.incrementAndGet()

        if (value % 500 == 0) {
            fileWriter.send(value)
        }
    }

    println("Numarator = $counter")
}