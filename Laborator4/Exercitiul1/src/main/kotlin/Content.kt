class Content{
    private var author: String = ""
    private var text: String = ""
    private var name: String = ""
    private var publisher: String = ""

    fun getAuthor(): String {
        return author
    }

    fun setAuthor(newAuthor: String) {
        author = newAuthor
    }

    fun getText(): String {
        return text
    }

    fun setText(newText: String) {
        text = newText
    }

    fun getName(): String {
        return name
    }

    fun setName(newName: String) {
        name = newName
    }

    fun getPublisher(): String {
        return publisher
    }

    fun setPublisher(newPublisher: String) {
        publisher = newPublisher
    }
}