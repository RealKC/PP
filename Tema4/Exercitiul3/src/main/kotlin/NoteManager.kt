import java.io.File

class NoteManager {
    private val notes: MutableList<Note> = mutableListOf()
    private var currentId = 1

    init {
        val notesDirectory = File("notes/")
        for (userDirectory in notesDirectory.listFiles()!!) {
            if (!userDirectory.isDirectory) {
                continue
            }

            val user = User(userDirectory.name)

            for (note in userDirectory.listFiles()!!) {
                val id = note.name.replace(".txt", "").toInt()
                currentId = id
                notes.add(Note.fromString(user, id, note.readText()) ?: continue)
            }
        }
    }

    fun createNote(user: User, title: String, date: Date, time: Time, contents: String): Note {
        val note = Note(user, ++currentId, title, date, time, contents)
        notes.add(note)

        return note
    }

    fun deleteNote(user: User, id: Int) {
        for (note in notes) {
            if (note.getId() == id && note.getUser() == user) {
                val file = File(note.getPath())
                file.delete()
            }
        }
    }

    fun getNotesFor(user: User): List<Note> {
        val notesForUser = mutableListOf<Note>()

        for (note in notes) {
            if (note.getUser() == user) {
                notesForUser.add(note)
            }
        }

        return notesForUser
    }

    fun getNote(user: User, id: Int): Note? {
        for (note in notes) {
            if (note.getUser() == user && note.getId() == id) {
                return note
            }
        }

        return null
    }

    fun writeToDisk() {
        for (note in notes) {
            val file = File(note.getPath())
            println(note)
            file.writeText(note.serialized())
        }
    }
}