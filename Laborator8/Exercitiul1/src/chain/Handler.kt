package chain

interface Handler {
    fun handleRequest(forwardDirection: String, messageToBeProcessed: String)

    fun setNext1(handler: Handler?)
    fun setNext2(handler: Handler?)
}