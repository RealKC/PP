package factory

class FactoryProducer {
    fun getFactory(choice: String): AbstractFactory {
        return when (choice.lowercase()) {
            "happyworker" -> HappyWorkerFactory()
            "elite" -> EliteFactory()
            else -> throw RuntimeException("Invalid choice: '$choice'")
        }

    }
}