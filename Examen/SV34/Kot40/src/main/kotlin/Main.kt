import java.io.File

fun main(args: Array<String>) {
    val file = File("text.txt")
    val out = File("output.txt")

    out.writeText("")
    file.forEachLine {
        it.splitToSequence(Regex("\\s")).forEach { w ->
            out.appendText(if (w.length < 4) w else w.substring(2))
            out.appendText(" ")
        }
        out.appendText("\n")
    }
}