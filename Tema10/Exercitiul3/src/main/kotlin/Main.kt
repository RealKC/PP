import kotlinx.coroutines.*
import kotlinx.coroutines.channels.Channel
import kotlinx.coroutines.channels.Channel.Factory.UNLIMITED
import java.util.concurrent.ConcurrentLinkedQueue
import java.util.concurrent.LinkedBlockingQueue
import kotlin.concurrent.thread
import kotlin.math.abs
import kotlin.random.Random

sealed class Message {
    class Number(val n: Int) : Message()
    object End : Message()
}

suspend fun gauss(queue: Channel<Message>) {
    println("coroutine started")
    while (true) {
        when (val message = queue.receive()) {
            is Message.Number -> {
                val n = message.n
                println("[coroutine] for $n the response is: ${((n + 1) * n) / 2}")
            }
            is Message.End -> break
        }

    }
    println("coroutine exited")
}

fun coroutines(end: Int): Unit = runBlocking {
    val scope = CoroutineScope(newFixedThreadPoolContext(2, "pool"))

    val channel = Channel<Message>(capacity = UNLIMITED)

    val jobs = List(4) { scope.launch { gauss(channel) } }

    for (i in 0..end) {
        channel.send(Message.Number(i))
    }

    repeat (4) { channel.send(Message.End) }

    jobs.forEach { it.join() }

    println("lol")
}

fun threads(end: Int) {
    val queue = LinkedBlockingQueue<Message>()

    for (i in 0..3) {
        thread {
            var message = queue.take()
            while (true) {
                when (message) {
                    is Message.Number -> {
                        val n = message.n
                        println("[thread] for $n the response is: ${((n + 1) * n) / 2}")
                    }
                    is Message.End -> break
                }
                message = queue.take()
            }
        }
    }

    for (i in 0..end) {
        queue.add(Message.Number(i))
    }
}

fun main() = with(abs(Random.nextInt() % 100)) {
    threads(this)
    coroutines(this)
}