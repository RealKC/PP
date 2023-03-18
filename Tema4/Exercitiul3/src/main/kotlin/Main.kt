import java.util.Scanner

fun main(args: Array<String>) {
    val stdin = Scanner(System.`in`)
    val noteManager = NoteManager()

    println("Welcome to the note Manager!")
    print("Enter your username: ")
    val username = stdin.nextLine()
    val user = User(username)

    println("Choose an option: ")
    println("1. Show all notes for your user")
    println("2. Show a specific note")
    println("3. Create a new note")
    println("4. Delete a note")
    print("Choice: ")

    when (stdin.nextInt()) {
        1 -> noteManager.getNotesFor(user).forEach { println("${it.getId()}# ${it.getTitle()} at ${it.getTime()} on ${it.getDate()}") }
        2 -> {
            print("Insert the note's id: ")
            val note = noteManager.getNote(user, stdin.nextInt())
            if (note == null) {
                println("Invalid note!")
            } else {
                print(note.toString())
            }
        }
        3 -> {
            println("Insert title: ")
            stdin.skip("\n")
            val title = stdin.nextLine()
            println("Insert contents: ")
            val contents = stdin.nextLine()
            noteManager.createNote(user, title, Date.now(), Time.now(), contents)
        }
        4 -> {
            print("Insert the note's id: ")
            noteManager.deleteNote(user, stdin.nextInt())
        }
        else -> println("Invalid option")
    }

    noteManager.writeToDisk()
}