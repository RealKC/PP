class Note(
    private val user: User,
    private val id: Int,
    private val title: String,
    private val date: Date,
    private val time: Time,
    private val contents: String,
) {
    companion object {
        fun fromString(user: User, id: Int, rawContents: String): Note? {
            val components = rawContents.split("---\n")
            if (components.size < 2) {
                return null
            }
            val header = components[0]
            val contents = components[1]

            val headerComponents = header.split("|")
            if (headerComponents.size < 3) {
                return null
            }
            return Note(
                user,
                id,
                headerComponents[0],
                Date.fromString(headerComponents[1]) ?: return null,
                Time.fromString(headerComponents[2]) ?: return null,
                contents
            )
        }
    }

    fun getId(): Int = id

    fun getUser(): User = user

    fun getTitle(): String = title

    fun getDate(): Date = date

    fun getTime(): Time = time

    fun getPath(): String = "${user.notePath()}/$id.txt"

    fun serialized(): String = "$title|$date|$time\n---\n$contents"

    override fun toString(): String {
        return """
            $title on $date at $time
            
            $contents
        """.trimIndent()
    }
}