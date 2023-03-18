class User(private val name: String) {
    fun notePath(): String {
        return "notes/$name/"
    }

    override fun equals(other: Any?): Boolean {
        if (other == null) {
            return false
        }

        if (other !is User) {
            return false
        }

        return name == other.name
    }
}