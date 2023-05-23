import java.io.File
import java.util.Scanner

fun rotn(s: String, n: Int) = s.map {
    val x = it + n
    val limit = if (it.isUpperCase()) 'Z' else 'z'
    when {
        it.isLetter() -> if (x > limit) x - 26 else x
        else -> it
    } }.fold("") { acc, ch -> acc + ch }

fun main(args: Array<String>) {
    print("Input the offset to rotate words by: ")
    val n = Scanner(System.`in`).nextInt()

    val file = File("loremipsum.txt")
    file.forEachLine { line ->
        line.split(" ")
            .map { if (it.length in 4..7) rotn(it, n) else it }
            .forEach { print("$it ") }
    }
}
