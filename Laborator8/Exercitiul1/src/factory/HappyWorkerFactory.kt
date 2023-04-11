package factory

import chain.Handler
import chain.HappyWorkerHandler

class HappyWorkerFactory: AbstractFactory() {
    override fun getHandler(handler: String): Handler {
        if (handler.lowercase() != "happyworker") {
            throw RuntimeException("Invalid parameter $handler")
        }

        return HappyWorkerHandler()
    }
}