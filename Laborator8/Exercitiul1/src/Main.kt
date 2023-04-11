import factory.FactoryProducer

fun main() {
    // se creeaza 1xFactoryProducer, 1xEliteFactory, 1xHappyWorkerFactory
    val factoryProducer = FactoryProducer()
    val eliteFactory = factoryProducer.getFactory("elite")
    val happyWorkerFactory = factoryProducer.getFactory("happyWorker")

    // crearea instantelor (prin intermediul celor 2 fabrici):
    // 2xCEOHandler, 2xExecutiveHandler, 2xManagerHandler, 2xHappyWorkerHandler
    val ceoHandler1 = eliteFactory.getHandler("ceo")
    val ceoHandler2 = eliteFactory.getHandler("ceo")
    val executiveHandler1 = eliteFactory.getHandler("executive")
    val executiveHandler2 = eliteFactory.getHandler("executive")
    val managerHandler1 = eliteFactory.getHandler("manager")
    val managerHandler2 = eliteFactory.getHandler("manager")
    val happyWorkerHandler1 = happyWorkerFactory.getHandler("happyWorker")
    val happyWorkerHandler2 = happyWorkerFactory.getHandler("happyWorker")

    // se construieste lantul (se verifica intai diagrama de obiecte si se realizeaza legaturile)
    ceoHandler1.setNext1(executiveHandler1)
    ceoHandler1.setNext2(ceoHandler2)
    executiveHandler1.setNext1(managerHandler1)
    executiveHandler1.setNext2(executiveHandler2)
    managerHandler1.setNext1(happyWorkerHandler1)
    managerHandler1.setNext2(managerHandler2)
    happyWorkerHandler1.setNext2(happyWorkerHandler2)
    ceoHandler2.setNext1(ceoHandler1)
    ceoHandler2.setNext2(executiveHandler2)
    executiveHandler2.setNext1(executiveHandler1)
    executiveHandler2.setNext2(managerHandler2)
    managerHandler2.setNext1(managerHandler1)
    managerHandler2.setNext2(happyWorkerHandler2)
    happyWorkerHandler2.setNext1(happyWorkerHandler1)

    // se executa lantul utilizand atat mesaje de prioritate diferita, cat si directii diferite in lant
    ceoHandler1.handleRequest("down", "4:Terminare a contractului de munca")
    ceoHandler1.handleRequest("right", "3:Cresterea a salariului")
    ceoHandler2.handleRequest("up", "2:Engage in layoffs")
}