package mike.tuiasi.ro

class Numarator {
    private var number: Int = 0
    private val observers: MutableList<NumaratorObserver> = mutableListOf()

    class CounterEvent(val number: Int)

    fun addObserver(obs: NumaratorObserver) {
        observers.add(obs)
    }

    fun increment() {
        number++

        val event = CounterEvent(number)

        for (obs in observers) {
            obs.notify(event)
        }
    }
}