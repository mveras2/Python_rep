from Classes.Conta1 import Conta1
from Classes.Poupanca import Poupanca

class ContaRemuneradaPoupanca(Conta1, Poupanca):

    def __init__(self, cliente, numero, saldo, taxa_remuneracao):
        Conta1.__init__(self, cliente, numero, saldo)
        Poupanca.__init__(self, taxa_remuneracao)
    

    def remuneraConta(self):
        self._Conta1__saldo += self._Conta1__saldo * (self._Poupanca__taxa_remuneracao/30)
