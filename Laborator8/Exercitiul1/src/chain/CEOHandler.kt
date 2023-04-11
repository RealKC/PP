package chain

class CEOHandler(private var next1: Handler? = null, private var next2: Handler? = null): Handler {
    override fun handleRequest(forwardDirection: String, messageToBeProcessed: String) {
        val message = messageToBeProcessed.split(':')
        val priority = message[0].toInt()

        if (priority == 1) {
            when (forwardDirection) {
                "up" -> next1!!.handleRequest("right", messageToBeProcessed)
                "down" -> next2!!.handleRequest("none", messageToBeProcessed)
                else -> println("Sunt CEO si procesez mesajul ${message[1]}")
            }
        } else {
            when (forwardDirection) {
                "right", "up" -> next1!!.handleRequest("right", messageToBeProcessed)
                "down" -> next2!!.handleRequest("right", messageToBeProcessed)
            }
        }
    }

    override fun setNext1(handler: Handler?) {
        next1 = handler
    }

    override fun setNext2(handler: Handler?) {
        next2 = handler
    }
}