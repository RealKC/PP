class Parser {
    val lexemes: List<Token>
    var lexemePos = 0

    constructor(expression: String) {
        lexemes = lexExpression(expression)
    }

    fun parse(): Expr {
        return term()
    }

    private fun term(): Expr {
        var expr = factor()

        while (matches(TokenType.MINUS, TokenType.PLUS)) {
            val operator = lexemes[lexemePos].type
            lexemePos++
            val right = term()
            expr = Expr.Binary(expr, operator, right)
        }

        return expr
    }

    private fun factor(): Expr {
        var expr = primary()

        while (matches(TokenType.DIVIDE, TokenType.MULTIPLY)) {
            val operator = lexemes[lexemePos].type
            lexemePos++
            val right = term()
            expr = Expr.Binary(expr, operator, right)
        }

        return expr
    }

    private fun primary(): Expr {
        val currentLexeme = lexemes[lexemePos]

        if (currentLexeme.type == TokenType.CONSTANT) {
            lexemePos++
            return Expr.Constant(currentLexeme.value!!)
        }

        if (currentLexeme.type == TokenType.LPAREN) {
            lexemePos++
            val expr = term()
            assert(lexemes[lexemePos].type == TokenType.RPAREN)
            lexemePos++
            return expr
        }

        throw RuntimeException("We shouldn't get here")
    }

    private fun matches(vararg tokens: TokenType): Boolean {
        if (lexemePos == lexemes.size)
            return false

        for (token in tokens) {
            if (lexemes[lexemePos].type == token) {
                return true
            }
        }

        return false
    }
}

sealed class Expr {
    class Binary(val left: Expr, val operator: TokenType, val right: Expr) : Expr() {
        override fun evaluate(): Double {
            return when (operator) {
                TokenType.PLUS -> left.evaluate() + right.evaluate()
                TokenType.MINUS -> left.evaluate() - right.evaluate()
                TokenType.MULTIPLY -> left.evaluate() * right.evaluate()
                TokenType.DIVIDE -> left.evaluate() / right.evaluate()
                else -> throw RuntimeException("How did you get here?")
            }
        }

        override fun toString(): String {
            return "Binary(left=$left, operator=$operator, right=$right)"
        }
    }

    class Constant(val value: Double) : Expr() {
        override fun evaluate(): Double {
            return value
        }

        override fun toString(): String {
            return "Constant(value=$value)"
        }
    }

    abstract fun evaluate(): Double
}