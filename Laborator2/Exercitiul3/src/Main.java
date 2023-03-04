import org.graalvm.polyglot.*;

import java.util.ArrayList;

class Polyglot {
    private static ArrayList<Integer> removeUpperAndLower20Percent(ArrayList<Integer> list) {
        Context polyglot = Context.newBuilder().allowAllAccess(true).build();

        Value result = polyglot.eval("R", """
        removeElems <- function(list) {
            list <- sapply(list, function(e) { e })
            list <- sort(list)
            list <- list[4:16]
            
            print("Media este: ")
            print(mean(list))
            
            return(list)
        }
        """).execute(list);

        ArrayList<Integer> out = new ArrayList<>();

        for (int i = 0; i < result.getArraySize(); ++i) {
            out.add(result.getArrayElement(i).asInt());
        }

        polyglot.close();

        return out;
    }

    private static ArrayList<Integer> generateRandomNumbers() {
        Context polyglot = Context.newBuilder().allowAllAccess(true).build();

        Value result = polyglot.eval("python", """
from random import randrange
list = []
for i in range(20):
    list.append(randrange(50000))
list
        """);

        ArrayList<Integer> list = new ArrayList<>();

        for (int i = 0; i < result.getArraySize(); ++i) {
            list.add(result.getArrayElement(i).asInt());
        }

        polyglot.close();

        return list;
    }

    private static void printArrayList(ArrayList<Integer> list) {
        Context polyglot = Context.newBuilder().allowAllAccess(true).build();

        polyglot.eval("js", """
        function printList(list) {
            for (const elem of list) {
                console.log(elem);
            }
        }
        printList
        """).executeVoid(list);

        polyglot.close();
    }

    public static void main(String[] args) {
        Context polyglot = Context.create();
        ArrayList<Integer> array = generateRandomNumbers();
        array = removeUpperAndLower20Percent(array);
        printArrayList(array);

        polyglot.close();
    }
}

