import java.util.Date

class Time(private val hour: Int, private val minute: Int, private val second: Int) {
    companion object {
        fun fromString(string: String): Time? {
            val components = string.split(":").map { it.trim() }
            if (components.size < 3) {
                return null
            }

            return Time(components[0].toInt(), components[1].toInt(), components[2].toInt())
        }

        fun now(): Time {
            val javaNow = Date()

            return Time(javaNow.hours, javaNow.minutes, javaNow.seconds)
        }
    }

    override fun toString(): String = "$hour:$minute:$second"
}