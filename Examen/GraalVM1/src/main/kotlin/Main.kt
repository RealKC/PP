import org.graalvm.polyglot.Context
import org.graalvm.polyglot.HostAccess
import org.graalvm.polyglot.PolyglotAccess
import org.graalvm.polyglot.Source
import java.io.File
import org.graalvm.polyglot.Value
import java.time.LocalDateTime

fun listFiles(context: Context): Value = context.eval("python",
        """
import subprocess

proc = subprocess.run(['/usr/bin/ls', '-lah'], capture_output=True)

proc.stdout.decode().split('\n')
"""
)

fun filterFiles(files: Value): List<String> {
    val res = mutableListOf<String>()

    for (i in 0 until files.arraySize) {
        val file = files.getArrayElement(i).asString()

        val components = file.split(' ')

        if (components.size <= 8) {
            continue;
        }
        val now = LocalDateTime.now().hour
        val fileHour = components[7].split(':')[0].toInt()

        if (fileHour - now <= 3)
            res.add(file)
    }

    return res
}

fun makePathsAbsolute(context: Context, files: List<String>): Value = context.eval("R", """
    makePathsAbsolute <- function(list) {
        list <- lapply(list, function(e) { e }) # This line turns graal values into R values
        list <- lapply(list, function(file) {
            components <- strsplit(file, "\\s")
            # R-ul asta m-o batut, nici eu nu inteleg de ce sunt chestiile astea
            components[[1]][9] <- normalizePath(components[[1]][9])
            return(unlist(c(components)))
        })
        return(list)
    }
""".trimIndent()).execute(files)

fun showFiles(context: Context, files: Value) {
    context.eval("js", """
        function showFiles(files) {
            for (const file of files) {
                const path = file.toString().split(',')[8]
                console.log(`file is ${'$'}{path}`)
            }
        }
        
        showFiles
    """.trimIndent()).execute(files)
}

fun main(args: Array<String>) {
    val polyglot = Context
            .newBuilder()
            .allowAllAccess(true)
            .build()

    val files = listFiles(polyglot)
    val filtered = filterFiles(files)
    val transformed = makePathsAbsolute(polyglot, filtered)
    showFiles(polyglot, transformed)
}