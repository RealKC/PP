import java.util.*

fun main() {
    val reader = Scanner(System.`in`)

    print("Enter a mathematical expression: ")

    val expr = reader.next()

    val parser = Parser(expr)
    val tree = parser.parse()

    println("$expr = ${tree.evaluate()}")
}
