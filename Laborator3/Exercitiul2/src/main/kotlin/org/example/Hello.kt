package org.example

import java.io.File
import java.util.*

fun updateDictionaryFromScanner(dictionary: HashMap<String, String>, input: Scanner) {
    try {
        var line = input.nextLine()
        while (line.length >= 3) {
            val words = line.split('=');
            dictionary[words[0]] = words[1]
            line = input.nextLine()
        }
    } catch (except: java.lang.Exception) {
        // ignore
    }
}

fun main(args: Array<String>) {
    val dictionar = hashMapOf<String, String>(
        "Once" to "Odata",
        "upon" to "ca",
        "a" to "",
        "time" to "niciodata",
        "there" to "acolo",
        "was" to "a fost",
        "an" to "o",
        "old" to "batrana",
        "woman" to "femeie",
        "who" to "care",
        "loved" to "iubea",
        "baking" to "sa gateasca",
        "gingerbread" to "turta dulce",
        "She" to "Ea",
        "would" to "ar fi",
        "bake" to "gatit",
        "gingerbread" to "turta dulce",
        "cookies" to "biscuiti",
        "cakes" to "prajituri",
        "houses" to "case",
        "and" to "si",
        "people" to "oameni",
        "all" to "toti",
        "decorated" to "decorati",
        "with" to "cu",
        "chocolate" to "ciocolata",
        "peppermint" to "menta",
        "caramel" to "caramel",
//        "candies" to "bomboane",
//        "colored" to "colorate",
//        "ingredients" to "ingrediente"
    )

    print("Doriti sa adaugati cuvinte noi in dictionar? [y/f/N] ")
    var stdin = Scanner(System.`in`)
    val choice = stdin.nextLine().getOrElse(0) { _ -> 'n' }
    if (choice.lowercase() == "y") {
        println("Inserati cuvintele si o linie goala cand ati terminat (separati cuvantul netradus de cunvatul tradus cu =): ")
        updateDictionaryFromScanner(dictionar, stdin)
    } else if (choice.lowercase() == "f") {
        print("Introduceti calea catre fisier: ")
        val path = stdin.next()
        updateDictionaryFromScanner(dictionar, Scanner(File(path)))
    }

    val poveste =
        "Once upon a time there was an old woman who loved baking gingerbread. She would bake gingerbread cookies, cakes, houses and gingerbread people, all decorated with chocolate and peppermint, caramel candies and colored ingredients."

    val words1 = poveste.split(" ")
    println("Cuvintele din poveste [${words1.count()}]:")

    for (word in words1)
        print("$word ")

    val words2 = mutableListOf<String>()
    for (word in words1) {
        words2.add(word.trim(',', '.'))
    }

    println("\n")
    println("Povestea tradusa ar suna cam asa:")

    val out = File("poveste.txt")

    for (item in words2) {
        if (dictionar.contains(item)) {
            print(dictionar[item])
            out.writeText(text = dictionar[item]!!)
        } else {
            print("[$item]")
            out.writeText(text = "[$item]")
        }
        print(" ")
        out.writeText(text = " ")
    }


}
