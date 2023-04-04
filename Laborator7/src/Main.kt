import java.io.File
import java.util.Scanner

class SyslogRecord(line: String) {
    private val timestamp: String
    private val hostname: String
    val processName: String
    var pid: Int = -1
    val logEntry: String

    init {
        timestamp = line.substring(0..15)

        val hostnameEnd = line.substring(17).withIndex().find { it.value.isWhitespace() }!!.index + 16
        hostname = line.substring(16..hostnameEnd)

        val processNameEnd = line.substring(hostnameEnd + 1).withIndex().find { it.value == ':' }!!.index + hostnameEnd
        val rawProcessName = line.substring(hostnameEnd + 2..processNameEnd)

        if (rawProcessName[rawProcessName.length - 1] == ']') {
            // we have a PID
            val splitLine = rawProcessName.split('[')
            processName = splitLine[0]
            pid = splitLine[1].substringBefore(']').toInt()
        } else {
            processName = rawProcessName
        }

        logEntry = line.substring(processNameEnd + 3)
    }

    override fun toString(): String {
        return "@ $timestamp on $hostname process $processName(PID=$pid) logged: $logEntry"
    }
}

fun main() {
    val file = Scanner(File("syslog"))
    val syslogEntries = mutableMapOf<String, MutableList<SyslogRecord>>()

    for (i in 0..30) {
        val line = file.nextLine()
        val entry = SyslogRecord(line)

        if (syslogEntries.contains(entry.processName)) {
            syslogEntries[entry.processName]!!.add(entry)
        } else {
            syslogEntries[entry.processName] = mutableListOf(entry)
        }
    }

    for (entry in syslogEntries) {
        entry.value.sortBy { it.logEntry }
    }

    syslogEntries.forEach { (_, entries) ->
        entries.forEach {
            if (it.pid != -1) {
                println(it)
            }
        }
    }
}