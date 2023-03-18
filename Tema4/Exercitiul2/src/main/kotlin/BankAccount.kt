import java.time.LocalDate

typealias Date = LocalDate

class BankAccount(
    private var availableAmount: Double,
    private val cardNumber: String,
    private val expirationDate: Date,
    private val cvvCode: Int,
    private val userName: String,
) {
    /**
     * Update the available amount of this account by [delta]
     * @return Whether the update was successful or not (a possible reason why
     * an update may not be successful is if the account's balance is insufficient)
     */
    fun updateAmount(delta: Double): Boolean {
        if (delta > availableAmount) {
            return false
        }

        availableAmount -= delta
        return true
    }
}