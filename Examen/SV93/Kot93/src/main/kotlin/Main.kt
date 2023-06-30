import kotlinx.coroutines.*
import kotlinx.coroutines.channels.Channel
import kotlinx.coroutines.channels.actor

open class Operatii(private val hashMap: HashMap<Int, Int>) {
    protected fun doSum() = hashMap.map { it.key + it.value }.toList()
    protected fun doSubtract() = hashMap.map { it.key - it.value }.toList()
    protected fun doMultiply() = hashMap.map { it.key * it.value }.toList()
    protected fun doDivide() = hashMap.map { it.key / it.value }.toList()
}

class Message(val list: CompletableDeferred<List<Int>>)

class SumActor(hashMap: HashMap<Int, Int>) : Operatii(hashMap) {
    suspend fun performWork(channel: Channel<Message>) {
        for (msg in channel) {
            msg.list.complete(doSum())
        }
    }
}

class SubstractionActor(hashMap: HashMap<Int, Int>) : Operatii(hashMap) {
    suspend fun performWork(channel: Channel<Message>) {
        for (msg in channel) {
            msg.list.complete(doSubtract())
        }
    }
}

class MultiplicationActor(hashMap: HashMap<Int, Int>) : Operatii(hashMap) {
    suspend fun performWork(channel: Channel<Message>) {
        for (msg in channel) {
            msg.list.complete(doMultiply())
        }
    }
}

class DivisionActor(hashMap: HashMap<Int, Int>) : Operatii(hashMap) {
    suspend fun performWork(channel: Channel<Message>) {
        for (msg in channel) {
            msg.list.complete(doDivide())
        }
    }
}

fun CoroutineScope.sumActor(hashMap: HashMap<Int, Int>) = actor<Message> {
    SumActor(hashMap).performWork(channel)
}

fun CoroutineScope.subActor(hashMap: HashMap<Int, Int>) = actor<Message> {
    SubstractionActor(hashMap).performWork(channel)
}

fun CoroutineScope.mulActor(hashMap: HashMap<Int, Int>) = actor<Message> {
    MultiplicationActor(hashMap).performWork(channel)
}

fun CoroutineScope.divActor(hashMap: HashMap<Int, Int>) = actor<Message> {
    DivisionActor(hashMap).performWork(channel)
}

fun main(args: Array<String>) = runBlocking<Unit> {
    val data = hashMapOf(
        1 to 15,
        2 to 22,
        3 to 333,
        4 to 41,
        5 to 5
    )

    val channels = listOf(
        sumActor(data),
        mulActor(data),
        divActor(data),
        subActor(data),
    )

    val answers = List(4) { CompletableDeferred<List<Int>>() }

    channels.zip(answers).map { it.first.send(Message(it.second)) }

    for ((idx, answer) in answers.map { it.await() }.withIndex()) {
        data.putAll(answer.chunked(2) { (idx * 1000 + it[0]) to it.getOrElse(1) { 0 } }.toMap())
    }

    println(data)
}