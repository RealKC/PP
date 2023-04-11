class Originator(private var message: String): Observable() {
    fun saveToMemento(): Memento = Memento(message)

    fun restoreFromMemento(memento: Memento) {
        message = memento.getState()
    }

    fun setMessage(message: String) {
        this.message = message
    }
}