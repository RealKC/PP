class Book(author: String, text: String, name: String, publisher: String) {
    private val content: Content = Content()

    init {
        content.setAuthor(author)
        content.setText(text)
        content.setName(name)
        content.setPublisher(publisher)
    }

    override fun toString(): String {
        return "${content.getName()} by ${content.getAuthor()}, published by ${content.getPublisher()}\n\n${content.getText()}"
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
}