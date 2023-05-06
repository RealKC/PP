import kotlinx.coroutines.CoroutineScope
import kotlinx.coroutines.channels.Channel
import kotlinx.coroutines.channels.Channel.Factory.UNLIMITED
import kotlinx.coroutines.launch
import kotlinx.coroutines.runBlocking
import java.util.concurrent.LinkedBlockingQueue
import kotlin.concurrent.thread
import kotlin.math.min
import kotlin.random.Random

sealed class Message {
    class Number(val n: Int) : Message()
    object End : Message()
}

fun log(msg: String, scope: CoroutineScope? = null) {
    when (scope) {
        null -> println("[in thread=${Thread.currentThread().name}] $msg")
        else -> println("[in coroutine=$scope] $msg")
    }
}

fun processWithThreads(list: List<Int>, alpha: Int) {
    val messageQueue = LinkedBlockingQueue<Message>()
    val queueOfSortedLists = LinkedBlockingQueue<List<Int>>()

    thread(name = "multiplication thread") {
        log("started multiplying")
        for (n in list) {
            messageQueue.put(Message.Number(n * alpha))
        }

        messageQueue.put(Message.End)
        log("finished multiplying")
    }

    thread(name = "sorting thread") {
        log("waiting for numbers")
        val unsortedList = mutableListOf<Int>()
        for (message in messageQueue) {
            when (message) {
                is Message.Number -> unsortedList.add(message.n)
                is Message.End -> break
            }
        }

        log("sorting")
        queueOfSortedLists.put(unsortedList.sorted().toList())
        log("finished sorting")
    }

    thread(name = "printing thread") {
        log("waiting for sorted list")
        val sortedList = queueOfSortedLists.take()
        println(sortedList)
    }
}

fun processWithCoroutines(list: List<Int>, alpha: Int) = runBlocking {
    val messageQueue = Channel<Message>(UNLIMITED)
    val sortedQueue = Channel<List<Int>>(1)

    launch {
        log("started multiplying", this)
        for (elem in list) {
            messageQueue.send(Message.Number(elem * alpha))
        }

        messageQueue.send(Message.End)
        log("finished multiplying", this)
    }

    launch {
        log("waiting for numbers", this)

        val multipliedNumbers = mutableListOf<Int>()
        for (msg in messageQueue) {
            when (msg) {
                is Message.Number -> multipliedNumbers.add(msg.n)
                is Message.End -> break
            }
        }

        log("sorting", this)
        sortedQueue.send(multipliedNumbers.sorted().toList())
        log("finished sorting", this)
    }

    runBlocking {
        log("waiting for sorted list", this)
        val sortedNumbers = sortedQueue.receive()
        println(sortedNumbers)
    }
}

fun main(args: Array<String>) {
    val elementCount = min(Random.nextInt(), 1000)
    val list = List(elementCount) { Random.nextInt() }
    val alpha = Random.nextInt()

    processWithThreads(list, alpha)
    processWithCoroutines(list, alpha)
}