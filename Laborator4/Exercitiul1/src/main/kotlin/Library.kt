class Library {
    private val books: MutableSet<Book> = mutableSetOf()

    fun getBooks(): Set<Book> {
        return books
    }

    fun addBook(book: Book) {
        books.add(book)
    }

    private fun findAllBy(predicate: (Book) -> Boolean): Set<Book> {
        val result = mutableSetOf<Book>()

        for (book in books) {
            if (predicate(book)) {
                result.add(book)
            }
        }

        return result

    }

    fun findAllByAuthor(author: String): Set<Book> {
        return findAllBy { it.hasAuthor(author) }
    }

    fun findAllByName(name: String): Set<Book> {
        return findAllBy { it.hasTitle(name) }
    }

    fun findAllByPublisher(publisher: String): Set<Book> {
        return findAllBy { it.isPublishedBy(publisher) }
    }

}