package mike.tuiasi.ro

class Receptor: NumaratorObserver {
    override fun notify(event: Numarator.CounterEvent) {
        println("Valoarea contorului este ${event.number}.")
    }
}