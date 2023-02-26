enum class TokenType {
    PLUS,
    MINUS,
    MULTIPLY,
    DIVIDE,
    CONSTANT,
    LPAREN,
    RPAREN,
}

class Token(
    val type: TokenType,
    val value: Double? = null,
) {
    override fun toString(): String {
        return "Token(type=$type, value=$value)"
    }
}

fun lexExpression(expression: String): List<Token> {
    val tokens = ArrayList<Token>()

    var i = 0

    while (i < expression.length) {
        when (expression[i]) {
            '+' -> {
                tokens.add(Token(TokenType.PLUS))
                i += 1
            }
            '-' -> {
                tokens.add(Token(TokenType.MINUS))
                i += 1
            }
            '/' -> {
                tokens.add(Token(TokenType.DIVIDE))
                i += 1
            }
            '*' -> {
                tokens.add(Token(TokenType.MULTIPLY))
                i += 1
            }
            '(' -> {
                tokens.add(Token(TokenType.LPAREN))
                i += 1
            }
            ')' -> {
                tokens.add(Token(TokenType.RPAREN))
                i += 1
            }
            else -> if (expression[i].isDigit()) {
                val maybeNumberEnd = expression.substring(i).withIndex().find { it.value.isDigit().not() }
                val numberEnd = if (maybeNumberEnd != null) maybeNumberEnd.index + i else expression.length
                tokens.add(Token(TokenType.CONSTANT, expression.substring(i until numberEnd).toDouble()))
                i = numberEnd
            }
            // we skip over whitespace and such
        }
    }

    return tokens
}