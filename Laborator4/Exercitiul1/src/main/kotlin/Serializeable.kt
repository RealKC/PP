interface Serializeable {
    fun toRaw(): String

    fun toHTML(): String

    fun toJSON(): String
}