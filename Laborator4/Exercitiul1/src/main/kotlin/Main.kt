fun main() {
    val library = Library()
    library.addBook(Book("Mircea", "In this Scroll of Magics I shall teach you fire", "1000 Ways to Burn Mana", "The Magic Books Association"))

    library.addBook(Book("Matei", "Mana is a very complex matter...", "Elementary Mana Manipulation, vol. 1", "The Magic Books Association"))
    library.addBook(Book("Matei", "Mana is a very complex matter...", "Elementary Mana Manipulation, vol. 2", "The Magic Books Association"))
    library.addBook(Book("Matei", "Mana is a very complex matter...", "Elementary Mana Manipulation, vol. 3", "The Magic Books Association"))

    library.addBook(Book("Eduard", "Kotlin is a complex language, but since it's been given sentience...", "Programming with Sentient Languages", "C.A.P. Industries"))

    LibraryPrinter.printBooksRaw(library.findAllByAuthor("Matei"))
    LibraryPrinter.printHTML(library.findAllByName("Programming with Sentient Languages"))
    LibraryPrinter.printJSON(library.findAllByPublisher("The Magic Books Association"))
    LibraryPrinter.printHTML(library.getBooks())
}