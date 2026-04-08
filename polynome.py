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
        for exp, coeff in enumerate(reversed(self.coeffiscients)):
            exp = len(self.coeffiscients) - exp - 1

            #Si le coefficient est non-nul
            if coeff != 0:

                #Trouver ce qui suit le coefficient et entrer dans la variable temporaire.
                match exp:
                    case 0:
                        temp = ""
                    case 1:
                        temp = "x"
                    case _:
                        temp = f"x^{exp}"
                
                #Si c'est le premier élément
                if expression == "":
                    if abs(coeff) == 1 and exp != 0:
                        temp = f"{coeff}".replace("1","") + temp
                    else:
                        temp = f"{coeff}{temp}"
                
                #Si ce n'est pas le premier élément
                else:
                    #si l'exposant est nul et le coefficient est unitaire, il peut seulement être +-1.
                    if abs(coeff) == 1 and exp == 0:
                        temp = "1"
                    
                    match coeff:
                        case 1:
                            temp = f" + {temp}"
                        case -1:
                            temp = f" - {temp}"
                        case _:
                            if coeff > 0:
                                temp = f" + {coeff}{temp}"
                            else:
                                temp = f" - {abs(coeff)}{temp}"
                expression += temp
        if len(expression) == 0:
            expression = "0"
        return expression

if __name__ == "__main__":
    exemple = Polynome([0])
    print(exemple.deriver())
    print(exemple)