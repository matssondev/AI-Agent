# calculator/pkg/calculator.py


class Calculator:
    def __init__(self):
        self.operators = {
            "+": lambda a, b: a + b,
            "-": lambda a, b: a - b,
            "*": lambda a, b: a * b,
            "/": lambda a, b: a / b,
        }
        self.precedence = {
            "+": 1,
            "-": 1,
            "*": 2,
            "/": 2,
        }

    def evaluate(self, expression):
        if not expression or expression.isspace():
            return None
        tokens = self._tokenize(expression)
        return self._evaluate_infix(tokens)

    def _tokenize(self, expression):
        # This implementation needs to be careful about negative numbers
        # and not split them.
        tokens = []
        i = 0
        while i < len(expression):
            char = expression[i]
            if char.isspace():
                i += 1
                continue
            elif char.isdigit() or (
                char == "-"
                and (
                    not tokens
                    or tokens[-1] in self.operators
                    or tokens[-1] == "("
                    or (
                        tokens[-1] == ")"
                        and i + 1 < len(expression)
                        and expression[i + 1].isdigit()
                    )
                )
                and (i + 1 < len(expression) and expression[i + 1].isdigit())
            ):
                # Handle numbers, including negative numbers
                j = i
                if char == "-":
                    j += 1
                while j < len(expression) and (
                    expression[j].isdigit() or expression[j] == "."
                ):
                    j += 1
                tokens.append(expression[i:j])
                i = j
            elif char in self.operators or char in "()":
                tokens.append(char)
                i += 1
            else:
                raise ValueError(f"Invalid character: {char}")
        return tokens

    def _evaluate_infix(self, tokens):
        values = []
        operators = []

        for token in tokens:
            if token == "(":
                operators.append(token)
            elif token == ")":
                while operators and operators[-1] != "(":
                    self._apply_operator(operators, values)
                if operators and operators[-1] == "(":
                    operators.pop()  # Pop the "("
                else:
                    raise ValueError("Mismatched parentheses")
            elif token in self.operators:
                while (
                    operators
                    and operators[-1] in self.operators
                    and self.precedence[operators[-1]] >= self.precedence[token]
                ):
                    self._apply_operator(operators, values)
                operators.append(token)
            else:
                try:
                    values.append(float(token))
                except ValueError:
                    raise ValueError(f"invalid token: {token}")

        while operators:
            if operators[-1] == "(":
                raise ValueError("Mismatched parentheses")
            self._apply_operator(operators, values)

        if len(values) != 1:
            raise ValueError("invalid expression")

        return values[0]

    def _apply_operator(self, operators, values):
        if not operators:
            return

        operator = operators.pop()
        if len(values) < 2:
            raise ValueError(f"not enough operands for operator {operator}")

        b = values.pop()
        a = values.pop()
        values.append(self.operators[operator](a, b))
