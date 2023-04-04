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

fun main(args: Array<String>) {
    val contents = File("history.log").readText()



    contents.split("\n\n").map { HistoryLogRecord(it) }.forEach { println(it) }

}