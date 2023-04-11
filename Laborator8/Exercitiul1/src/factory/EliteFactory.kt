package factory

import chain.CEOHandler
import chain.ExecutiveHandler
import chain.Handler
import chain.ManagerHandler

class EliteFactory: AbstractFactory() {
    override fun getHandler(handler: String): Handler {
        return when (handler.lowercase()) {
            "ceo" -> CEOHandler()
            "executive" -> ExecutiveHandler()
            "manager" -> ManagerHandler()
            else -> throw RuntimeException("Invalid handler $handler")
        }
    }
}