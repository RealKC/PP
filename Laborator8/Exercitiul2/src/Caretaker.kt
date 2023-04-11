class Caretaker {
    private val savedStates = mutableListOf<Memento>()

    fun addMemento(memento: Memento) {
        savedStates.add(memento)
    }

    fun getSavedStates(): List<Memento> = savedStates
}