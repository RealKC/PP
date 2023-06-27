import java.io.File

interface Writeable {
    fun write(fileName: String)
}

class MapWriteable<K, V>(private val map: Map<K, V>): Writeable {
    override fun write(fileName: String) {
        val file = File(fileName)
        file.appendText("{\n")
        for (entry in map) {
            file.appendText("\t'${entry.key}': ${entry.value},\n")
        }
        file.appendText("}\n")
    }
}

class StringWriteable(private val string: String): Writeable {
    override fun write(fileName: String) {
        File(fileName).appendText("$string\n")
    }
}

class ListWriteable<T>(private val list: List<T>): Writeable {
    override fun write(fileName: String) {
        val file = File(fileName)
        file.appendText(list.toString())
        file.appendText("\n")
    }
}

fun main() {
    val writeables = listOf(
        MapWriteable(mapOf(
            "1" to 5,
            "2" to 10,
            "3" to 15,
        )),
        StringWriteable("uwu OwO"),
        ListWriteable(listOf(true, false, true, false, false, true)),
    )

    for (writeable in writeables) {
        writeable.write("uwu.owo")
    }
}