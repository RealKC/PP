class LibraryPrinter {
    companion object {
        fun printBooksRaw(books: Set<Book>) {
            for (book in books) {
                println(book.toRaw())
            }
        }

        fun printHTML(books: Set<Book>) {
            for (book in books) {
                println(book.toHTML())
            }
        }

        fun printJSON(books: Set<Book>) {
            println("[")
            for (book in books) {
                println("${book.toJSON()}, ")
            }
            println("]")
        }
    }
}