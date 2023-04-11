package chain

class HappyWorkerHandler(private var next1: Handler? = null, private var next2: Handler? = null): Handler {
    override fun handleRequest(forwardDirection: String, messageToBeProcessed: String) {
        val message = messageToBeProcessed.split(':')
        val priority = message[0].toInt()

        if (priority == 4) {
            when (forwardDirection) {
                "up" -> next1!!.handleRequest("right", messageToBeProcessed)
                "down" -> next2!!.handleRequest("none", messageToBeProcessed)
                else -> println("Sunt 'Happy Worker' si procesez mesajul ${message[1]}")
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