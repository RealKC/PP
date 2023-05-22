fun main() {
    // Exercitiul 1
    val list = listOf(1, 21, 75, 39, 7, 2, 35, 3, 31, 7, 8)
    println("initial list = $list")
    val filtered = list.filter { it >= 5 }
    println("filtered = $filtered")
    val pairs = filtered.chunked(2).map { lst -> lst[0] to lst[1] }
    println("pairs = $pairs")
    val multiplied = pairs.map { it.first * it.second }
    println("multiplied = $multiplied")
    val summed = multiplied.sum()
    println("summed = $summed")
}