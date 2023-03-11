import org.jsoup.Jsoup
import org.jsoup.nodes.Document
import java.io.File

const val MAX_DEPTH = 2

class Node(
    private val url: String,
) {
    var children: MutableList<Node> = mutableListOf()

    fun populateChildren(depth: Int, baseUrl: String? = null) {
        if (depth == MAX_DEPTH) {
            return
        }

        val url = if (baseUrl != null) "$baseUrl${this.url}" else this.url

        val document = Jsoup.connect(url).get()
        for (url in getLocalUrls(document)) {
            var node = Node(url)
            node.populateChildren(depth + 1, document.baseUri())
            children.add(node)
        }
    }

    override fun toString(): String {
        return toStringWithDepth().toString()
    }

    private fun toStringWithDepth(depth: Int = 0): StringBuilder {
        var stringBuilder = StringBuilder()

        for (i in 0 until depth) {
            stringBuilder.append('\t')
        }
        stringBuilder.append("$url\n")
        for (child in children) {
            stringBuilder.append(child.toStringWithDepth(depth + 1))
        }

        return stringBuilder
    }
}

fun serializeTree(tree: Node, path: String? = null): String? {
    val serialized = tree.toString()
    if (path != null) {
        val file = File(path)
        val writer = file.writer()
        writer.write(serialized)
        writer.flush()
        writer.close()
        return null
    }

    return serialized
}

fun deserializeTree(str: String, isFile: Boolean): Node {
    val contents = if (isFile) File(str).readText() else str
    println(contents)
    val lines = contents.lines()

    var root = Node(lines.first()!!)
    var i = 1

    while (i < lines.size) {
        var currLine = lines[i]

        if (currLine.isBlank()) {
            break
        }

        assert(currLine.count { it == '\t' } == 1)

        var internalNode = Node(currLine.trim())

        i++
        currLine = lines[i]
        while (currLine.count { it == '\t' } == 2) {
            internalNode.children.add(Node(currLine.trim()))

            i++
            currLine = lines[i]
        }

        root.children.add(internalNode)
    }

    return root
}

fun main(args: Array<String>) {
    val path = "serialised.txt"
    if (!File(path).exists()) {
        var node = Node("https://gtk-rs.org/")
        node.populateChildren(0)

        serializeTree(node, path)
    } else {
        val deserialized = deserializeTree(path, true)
        println("Deserialized: $deserialized")
    }
}

fun getLocalUrls(document: Document): List<String> {
    var result = mutableListOf<String>()

    for (a in document.select("a")) {
        val href = a.attr("href")
        if (href.startsWith("/") && href.length > 1 && href.count { it == '/' } == 1) {
            result.add(href)
        }
    }

    return result
}