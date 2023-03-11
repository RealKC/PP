import java.io.File

fun main(args: Array<String>) {
    val bookLines = File("book.txt")
        .readLines()
        .map { it.replace(Regex("\\s+"), " ") }
        .filter { it.isNotEmpty() }
        .filterNot { Regex("\\d+").matchesAt(it, 1) }

    print(bookLines.joinToString("\n"))
}