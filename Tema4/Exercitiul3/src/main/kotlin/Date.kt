import java.util.Date as JavaDate

class Date(private val year: Int, private val month: Int, private val day: Int) {
    companion object {
        fun fromString(string: String): Date? {
            val components = string.split("-").map { it.trim() }
            if (components.size < 3) {
                return null
            }

            return Date(components[0].toInt(), components[1].toInt(), components[2].toInt())
        }

        fun now(): Date {
            val javaNow = JavaDate()

            return Date(javaNow.year, javaNow.month, javaNow.day)
        }
    }

    override fun toString(): String = "$year-$month-$day"
}