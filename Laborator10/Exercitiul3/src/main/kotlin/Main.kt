import java.io.File
import java.util.concurrent.Semaphore
import java.util.concurrent.locks.Lock
import java.util.concurrent.locks.ReentrantLock

class Log private constructor() {
    companion object {
        val instance = Log()
        val fname = "Semafor.txt"
    }

    fun write(line: String) {
        File(fname).appendText("$line\n")
    }

    fun reset() {
        File(fname).delete()
    }
}

class Semafor private constructor() {
    companion object {
        val instance = Semafor()
    }

    val lock: Lock = ReentrantLock()
    var counter = 1

    fun enter(): Boolean {
        lock.lock()
        if (counter <= 0) {
            lock.unlock()
            return false
        }

        counter--
        lock.unlock()
        return true
    }

    fun exit() {
        lock.lock()
        counter++
        lock.unlock()
    }
}

class SimpleThread : Thread() {
    override fun run() {
        if (Semafor.instance.enter()) {
            Log.instance.write("Instanta clasei derivate din Thread ${Thread.currentThread()} s -a executat .")
            Semafor.instance.exit()
        }
    }
}

class SimpleRunnable : Runnable {
    override fun run() {
        if (Semafor.instance.enter()) {
            Log.instance.write("Instanta clasei care implementeaza Runnable ${Thread.currentThread()} s -a executat .")
            Semafor.instance.exit()
        }
    }
}

fun main(args: Array<String>) {
    object : Thread() {
        override fun run() {
            if (Semafor.instance.enter()) {
                println("Sunt in thread-ul singleton ${Thread.currentThread()}")
                Semafor.instance.exit()
            }
        }
    }.start()

    val t1 = SimpleThread()
    t1.run()

    val t2 = SimpleRunnable()
    t2.run()

    val thread = Thread {
        if (Semafor.instance.enter()) {
            Log.instance.write("Thread lambda ${Thread.currentThread()} s-a executat .")
            Semafor.instance.exit()
        }
    }
    thread.start()
}