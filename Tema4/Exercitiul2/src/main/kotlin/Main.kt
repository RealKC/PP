import java.time.LocalDate
import java.util.Scanner

fun main(args: Array<String>) {
    val stdin = Scanner(System.`in`)

    val ticketManager = TicketManager(mapOf(
        "Frozen" to 35.0,
        "Dune" to 25.0,
        "Fast and Furious" to 60.0,
        "Star Wars CDXX" to 95.43,
    ))

    print("What movie do you wish to go to? ")
    val title = stdin.nextLine()

    print("Choose a payment method [card/cash]: ")
    val payment = when (stdin.next()) {
        "card" -> {
            println("Please insert your bank details: ")
            print("Account holder: ")
            val accountHolder = stdin.nextLine()
            print("Card number: ")
            val cardNumber = stdin.nextLine()
            print("Expiration date: ")
            val expirationDate = LocalDate.parse(stdin.next())
            print("Available amount: ")
            val availableAmount = stdin.nextDouble()
            print("CCV code: ")
            val ccvCode = stdin.nextInt()

            BankPayment(BankAccount(availableAmount, cardNumber, expirationDate, ccvCode, accountHolder))
        }
        "cash" -> {
            println("Please insert how much cash you have: ")
            CashPayment(stdin.nextDouble())
        }
        else -> {
            println("Invalid payment method")
            return
        }
    }

    val ticket = ticketManager.buyTicketFor(title, payment)

    if (ticket == null) {
        println("Invalid movie or not enough funds")
    } else {
        print(ticket)
    }
}