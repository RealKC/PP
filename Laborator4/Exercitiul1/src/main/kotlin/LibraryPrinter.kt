class LibraryPrinter {
    companion object {
        fun printBooksRaw(books: Set<Book>) {
            for (book in books) {
                println(book)
            }
        }

        fun printHTML(books: Set<Book>) {
            for (book in books) {
                println("<p><b>${book.getName()}</b>, by <i>${book.getAuthor()}</i>, published by ${book.getPublisher()}<br><details>${book.getContent()}</details></p>")
            }
        }

        fun printJSON(books: Set<Book>) {
            println("[")
            for (book in books) {
                println("""
                    {
                        "author": "${book.getAuthor()}",
                        "name": "${book.getAuthor()}",
                        "publisher": "${book.getPublisher()}",
                        "content": "${book.getContent()}",
                    },
                """.trimIndent())
            }
            println("]")
        }
    }
}