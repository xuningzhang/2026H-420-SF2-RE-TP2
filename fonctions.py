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
    pass


class Exp(Expression):
    """Expression representant exp(u)."""

    # Votre code ici (remplacer le "pass" par votre implementation)
    pass
