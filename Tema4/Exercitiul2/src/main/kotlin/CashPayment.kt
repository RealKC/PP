class CashPayment(private var availableAmount: Double): PaymentMethod {
    override fun pay(fee: Double): Boolean {
        if (fee > availableAmount) {
            return false
        }

        availableAmount -= fee
        return true
    }
}