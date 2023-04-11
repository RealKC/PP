open class Observable {
    private val observers = mutableListOf<Observer>()
    fun add(observer: Observer) {
        observers.add(observer)
    }

    fun remove(observer: Observer) {
        observers.remove(observer)
    }

    fun notifyAll() {
        for (observer in observers) {
            observer.update()
        }
    }
}