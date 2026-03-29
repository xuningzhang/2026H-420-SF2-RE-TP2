from expression import Expression

class Addition(Expression):
    """Expression representant u + v."""

    # Votre code ici (remplacer le "pass" par votre implementation)
    def __init__(self, u, v):
        self.u = u
        self.v = v

    def evaluer(self,x):
        return sum([function.evaluer(x) for function in [self.u, self.v]])
    
    def deriver(self):
        return Addition(self.u.deriver(), self.v.deriver())
    
    def __str__(self):
        return f"{self.u} + {self.v}"


class Multiplication(Expression):
    """Expression representant u * v."""

    # Votre code ici (remplacer le "pass" par votre implementation)
    pass
