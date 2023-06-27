
fun main(args: Array<String>) {
    var count = 0

    (2..100).forEach { i ->
        (i + 1..100).forEach {j ->
            (j + 1..100).forEach {
                count++
            }
        }
    }

    println("The number of subsets of A that contain 1 is $count")
}