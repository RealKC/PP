import java.io.File

class HistoryLogRecord(record: String) : Comparable<HistoryLogRecord> {
    var startDate: String = ""
    var commandLine: String = ""
    var requestedBy: String = ""
    var action: Pair<String, String>? = null
    var endDate: String = ""

    init {
        for (line in record.split('\n')) {
            if (line.isEmpty()) {
                continue
            }

            val type = line.split(':')[0].trim()

            val colonIdx = line.withIndex().find { it.value == ':' }!!.index + 2
            when (type) {
                "Start-Date" -> startDate = line.substring(colonIdx)
                "Commandline" -> commandLine = line.substring(colonIdx)
                "Requested-By" -> requestedBy = line.substring(colonIdx)
                "End-Date" -> endDate = line.substring(colonIdx)
                else -> action = Pair(type, line.substring(colonIdx))
            }
        }
    }

    override fun compareTo(other: HistoryLogRecord): Int = startDate.compareTo(other.startDate)

    override fun toString(): String {
        return buildString {
            append("Operation started on ")
            append(startDate)
            append(" and finished on ")
            append(endDate)
            append(", with metadata\n")

            if (commandLine.isNotEmpty()) {
                append("\tCommand line: ")
                append(commandLine)
                append('\n')
            }

            if (action != null) {
                append("\t${action!!.first}: ${action!!.second}\n")
            }

            if (requestedBy.isNotEmpty()) {
                append("\tRequested by: ")
                append(requestedBy)
            }

            append("\n")
        }
    }
}

fun <T: Comparable<T>> max(a: T, b: T): T {
    return if (a < b) {
        b
    } else {
        a
    }
}

fun <T: Comparable<T>> findAndReplace(target: T, replacement: T, collection: MutableMap<String, T>) {
    var targetKey: String? = null

    for (element in collection) {
        if (element.value == target) {
            targetKey = element.key
        }
    }

    if (targetKey != null) {
        collection[targetKey] = replacement
    }
}

fun main(args: Array<String>) {
    val contents = File("history.log").readText()
    val recordsList = contents.split("\n\n").map { HistoryLogRecord(it) }

    val records = mutableMapOf<String, HistoryLogRecord>()
    for (record in recordsList) {
        records[record.startDate] = record
    }

    println("""Max between 'a' and 'b' is 'c'
            - 'a' = ${recordsList[0]}
            - 'b' = ${recordsList[1]}
            - 'c' = ${max(recordsList[0], recordsList[1])}
    """.trimMargin())

    println("Original records: $records")
    findAndReplace(recordsList[0], recordsList[1], records)
    println("Modified records: $records")
}