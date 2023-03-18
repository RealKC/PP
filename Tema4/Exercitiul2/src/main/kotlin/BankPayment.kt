class BankPayment(private val bankAccount: BankAccount): PaymentMethod {
    override fun pay(fee: Double): Boolean {
        return bankAccount.updateAmount(-fee)
    }
}