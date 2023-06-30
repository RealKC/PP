package mike.tuiasi.ro

interface NumaratorObserver {
    fun notify(event: Numarator.CounterEvent)
}
