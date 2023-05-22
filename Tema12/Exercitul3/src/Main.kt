import java.io.File
import java.util.Scanner
import kotlin.math.pow
import kotlin.math.sqrt

data class Point(val x: Int, val y: Int) {
    fun distance(other: Point) = sqrt(((this.x - other.x).toDouble().pow(2) + (this.y - other.y).toDouble().pow(2)))
}

fun main(args: Array<String>) {
    val input = Scanner(File("input.txt"))

    val count = input.nextInt()

    val points = mutableListOf<Point>()
    repeat(count) {
        points.add(Point(input.nextInt(), input.nextInt()))
    }

    var perimiter = points.first().distance(points.last())
    perimiter += points.zipWithNext { a, b -> a.distance(b) }.sum()

    println("The perimiter is: $perimiter")
}