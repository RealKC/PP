package org.example

import org.example.RHistogram
import java.io.File

fun main(args: Array<String>) {
    val lines = File("Fisier.txt").reader().readText()
    val words = lines.split(" ")

    val trimmedWords = mutableListOf<String>()
    words.forEach {
        val filter = it.trim(',', '.', '"', '?', '!')
        trimmedWords += filter.lowercase()
        print("$filter ")
    }
    println("\n")

    val chars = mutableListOf<String>()
    trimmedWords.forEach {
        for (c in it) {
            if (c in 'a'..'z' || c in 'A'..'Z') {
                chars += c.uppercase()
                print(c.uppercase())
            }
        }
    }
    println("\n")

    RHistogram.buildHistogram(trimmedWords.toTypedArray(), "Words", true)
    RHistogram.buildHistogram(chars.toTypedArray(), "Chars", true)

    val uniqueWords = getUniqueWordCount(trimmedWords)

    print("Unique words: ")
    for (word in uniqueWords) {
        if (word.value == 1) {
            print("${word.key} ")
        }
    }
    println()

    val uniqueChars = getUniqueCharCount(chars)
    print("Unique chars: ")
    for (word in uniqueChars) {
        if (word.value == 1) {
            print(word.key)
        }
    }
    println()

}

fun getUniqueWordCount(allWords: List<String>): MutableMap<String, Int> {
    val result = mutableMapOf<String, Int>()

    for (word in allWords) {
        result.merge(word, 1, Int::plus)
    }

    return result
}

fun getUniqueCharCount(allChars: List<String>): MutableMap<Char, Int> {
    val result = mutableMapOf<Char, Int>()

    for (char in allChars) {
        result.merge(char[0], 1, Int::plus)
    }

    return result
}

//fun sortByHitCount