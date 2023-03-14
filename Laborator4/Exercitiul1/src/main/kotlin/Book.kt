class Book(author: String, text: String, name: String, publisher: String, private var price: Double): Serializeable {
    private val content: Content = Content()

    init {
        content.setAuthor(author)
        content.setText(text)
        content.setName(name)
        content.setPublisher(publisher)
    }

    override fun toString(): String {
        return "${content.getName()} by ${content.getAuthor()}, published by ${content.getPublisher()}, costs ${getPrice()} RON\n\n${content.getText()}"
    }

    fun getName(): String {
        return content.getName()
    }

    fun getAuthor(): String {
        return content.getAuthor()
    }

    fun getPublisher(): String {
        return content.getPublisher()
    }

    fun getContent(): String {
        return content.getText()
    }

    fun hasAuthor(author: String): Boolean {
        return getAuthor() == author
    }

    fun hasTitle(title: String): Boolean {
        return getName() == title
    }

    fun isPublishedBy(publisher: String): Boolean {
        return getPublisher() == publisher
    }

    fun getPrice(): Double {
        return price
    }

    fun setPrice(newPrice: Double) {
        price = newPrice
    }

    override fun toRaw(): String {
        return toString()
    }

    override fun toHTML(): String {
        return "<p><b>${getName()}</b>, by <i>${getAuthor()}</i>, published by ${getPublisher()}, costs ${getPrice()} RON<br><details>${getContent()}</details></p>"
    }

    override fun toJSON(): String {
        return """
            {
                "author": "${getAuthor()}",
                "name": "${getAuthor()}",
                "publisher": "${getPublisher()}",
                "content": "${getContent()}",
                "price": ${getPrice()},
                "currency": "RON"
            }
        """.trimIndent()
    }
}