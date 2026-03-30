from expression import Expression


class Polynome(Expression):
    """Polynome represente par une liste de coefficients [a0, a1, a2, ...]."""

    # Votre code ici (remplacer le "pass" par votre implementation)
    def __init__(self, coeffiscients: list[float | int]):
        self.coeffiscients = coeffiscients
    
    def evaluer(self, x: float) -> float:
        return sum([coeff * x ** exp for exp, coeff in enumerate(self.coeffiscients)])
    
    def deriver(self):
        f_derive = [exp*coeff for exp, coeff in enumerate(self.coeffiscients)]
        del f_derive[0]
        if len(f_derive) == 0:
            f_derive = [0]
        return Polynome(f_derive)
    
    def __str__(self):
        expression = ""
        for exp, coeff in enumerate(self.coeffiscients):
            if coeff != 0:
                match exp:
                    case 0:
                        exp = ""
                    case 1:
                        exp = "x"
                    case _:
                        exp = f"x^{exp}"
                if len(expression) == 0:
                    expression += f"{coeff}"+exp
                elif coeff > 0:
                    expression += f" + {coeff}"+exp
                else:
                    expression += f" - {abs(coeff)}"+exp
        if len(expression) == 0:
            expression = "0"
        return expression

if __name__ == "__main__":
    exemple = Polynome([1])
    print(exemple.deriver())
    print(exemple)
    x = input()