class TestFunctor<K, V>(val map: MutableMap<K, V>) {
    fun map(function: (K, V) -> Pair<K, V>) = TestFunctor(map.map { function(it.key, it.value) }.toMap(mutableMapOf()))
}

fun String.toPascalCase(): String = this.split(" ").joinToString(separator = "") { it.capitalize() }

fun main() {
    val map = mutableMapOf(
        1 to "hello",
        2 to "world",
        3 to "goodafternon",
        4 to "ilovekotlin"
    )

    var functor = TestFunctor(map)
    functor = functor.map { k, v -> Pair(k, "Test $v") }
    functor = functor.map { k, v -> Pair(k, v.toPascalCase())}

    println(functor.map)
}