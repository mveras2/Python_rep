import datetime
from Classes.Conta1 import Conta1

class ContaEspecial(Conta1):

    def __init__(self, clientes, numero, saldo, limite):
        super().__init__(clientes, numero, saldo)
        self.__limite = limite

    def sacar(self, valor):
    #para o saldo precisamos usar uma verificação de saldo válido
        if (self._Conta1__saldo + self.__limite) < valor:
                print(f"Não existe saldo suficiente na conta {self._Conta1__numero}, cliente {self._Conta1__clientes.get_nome()}")
                return False # Não tem saldo suficiente
        else: 
                self._Conta1__saldo -= valor
                #if (self.__saldo < 0):
                #    self.__limite += self.__saldo
                self._Conta1__extrato.transacoes.append(["Saque", valor, datetime.datetime.today()])  
                return True # Saque realizado com sucesso