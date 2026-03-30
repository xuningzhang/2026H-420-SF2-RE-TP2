from expression import Expression
from polynome import Polynome
from operations import Multiplication
import math


class Sin(Expression):
    """Expression representant sin(u)."""

    # Votre code ici (remplacer le "pass" par votre implementation)
    def __init__(self, function : "Polynome"):
        self.function = function
    
    def evaluer(self, x):
        return math.sin(self.function.evaluer(x))

    def deriver(self):
        return Cos(self.function)
    
    def __str__(self):
        return f"sin({self.function})"

class Cos(Expression):
    """Expression representant cos(u)."""

    # Votre code ici (remplacer le "pass" par votre implementation)
    def __init__(self, function : "Polynome"):
        self.function = function
    
    def evaluer(self, x):
        return math.cos(self.function.evaluer(x))

    def deriver(self):
        return Sin(Multiplication(Polynome([-1]),self.function))
    
    def __str__(self):
        return f"cos({self.function})"


class Exp(Expression):
    """Expression representant exp(u)."""

    # Votre code ici (remplacer le "pass" par votre implementation)
    def __init__(self, function : "Polynome"):
        self.function = function
    
    def evaluer(self, x):
        return math.e**(self.function.evaluer(x))

    def deriver(self):
        return Exp(self.function)
    
    def __str__(self):
        return f"e^({self.function})"

if __name__ == "__main__":
    exemple = [Cos(Polynome([1,2,3])),Sin(Polynome([1,2,3])),Exp(Polynome([1,2,3]))]
    for func in exemple:
        print(func)
        print(func.evaluer(1))
        print(func.deriver())
        print(func.deriver().evaluer(1))