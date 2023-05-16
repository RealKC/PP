import java.text.SimpleDateFormat
import java.util.Date
import java.util.Scanner
import kotlin.math.sqrt
import kotlin.properties.Delegates

// BEGIN - Exercitiul 1
fun Int.isPrime(): Boolean {
    if (this == 2) {
        return true
    }

    if (this % 2 == 0) {
        return false
    }

    val limit = sqrt(this.toDouble()).toInt()
    for (d in 3..limit step 2) {
        if (this % d == 0) {
            return false
        }
    }

    return true
}
// END - Exercitiul 1

// BEGIN - Exercitiul 2
fun String.toDate(format: String): Date = SimpleDateFormat(format).parse(this)
// END - Exercitiul 2

fun main() {
    // Exercitiul 1
    println("2 is prime? ${2.isPrime()}")
    println("3 is prime? ${3.isPrime()}")
    println("12 is prime? ${12.isPrime()}")

    // Exercitiul 2
    val date = "25/10/2002"
    println("The date is ${date.toDate("d/M/yyyy")}")

    // Exercitiul 3
    val set = mapOf(
        1 to "abc",
        2 to "def",
        3 to "ghi",
    )

    val iset = set.map {
        it.value to it.key
    }.toMap()

    println("mapped set was $iset")

    // Exercitiul 4
    var alwaysPrime: Int by Delegates.vetoable(2) { _, _, newValue ->
        newValue.isPrime()
    }

    println("alwaysPrime is $alwaysPrime")

    println("trying to set it to 6...")
    alwaysPrime = 6
    println("now it is $alwaysPrime")

    val stdin = Scanner(System.`in`)

    // Exercitiul 5
    print("n = ")
    val n = stdin.nextInt()

    val list = listOf(1, 2, 3)

    val repeated = list.flatMap { init ->
        List(n) { init }
    }

    println("Initial list was $list\nRepeated list is $repeated")

    // Exercitiul 6
    print("a string = ")
    var s = stdin.next()
    val uniq = s.toCharArray().distinct().fold("") { acc, c -> acc + c }
    println("$s => $uniq")

    // Exercitiul 7
    print("another string =")
    s = stdin.next()
    val reduced = s.toCharArray().fold(HashMap<Char, Int>()) { acc, c ->
        if (acc[c] == null) {
            acc[c] = 1
        } else {
            acc[c] = acc[c]!! + 1
        }

        acc
    }.toList().fold("") { acc, pair ->
        acc + if (pair.second > 1) {
            "${pair.first}${pair.second}"
        } else {
            "${pair.first}"
        }
    }

    print("$s -> $reduced")
}
