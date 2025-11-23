import datetime
from Classes.Extrato import Extrato


class Conta1: # Essa classe foi copiada do aqrquivo anterior, porém com alterações para se adequer a esse exercício

    def __init__(self, clientes, numero, saldo):    # a função def __init__ é chamada de construtor
        self.__clientes = clientes    # O uso do __ antes do atributo serve para torná-los privada
        self.__numero = numero
        self.__saldo = saldo
        self.__data_abertura = datetime.datetime.today()
        self.__extrato = Extrato()

    def depositar(self, valor):      # Novo método da classe - a função def cria um método. O Construtor é um método
        self.__saldo = self.__saldo + valor  # pode-se usar também : self.saldo += valor
        self.__extrato.transacoes.append(["Depósito", valor, datetime.datetime.today()])

    def sacar(self, valor):
        #para o saldo precisamos usar uma verificação de saldo válido
        if self.__saldo < valor:
                return False # Não tem saldo suficiente
        else: 
             self.__saldo -= valor
             self.__extrato.transacoes.append(["Saque", valor, datetime.datetime.today()])  
             return True # Saque realizado com sucesso
    
    def gerar_extrato(self):
        #print(f"Número da conta: {self.__numero}")
        #for cliente in self.__cliente:
        #    print(f"Titular: {cliente.get_nome()} - CPF: {cliente.get_cpf()}")
        #print(f"Saldo da conta: R${self.__saldo}")
      
        print(f"Nome do titular: {self.__clientes.get_nome()}\nCPF do titular: {self.__clientes.get_cpf()}")
        self.__extrato.gerar_extrato(self.__numero)
        print(f"Saldo final: R${self.__saldo}")

    def transfere_valor(self, conta_destino, valor):
        if self.__saldo < valor:
             return("Não existe saldo suficiente")
        else:
             conta_destino.depositar(valor)
             self.__saldo -= valor
             self.__extrato.transacoes.append(["Trasferência", valor, datetime.datetime.today()])  
             return("Transferência Realizada")
  
    #Esse é um modelo de encapsulamento para alterar a variável privado "saldo".
    @property
    def saldo(self):
         return self.__saldo
    
    @saldo.setter
    def saldo(self, valor):
            if(valor < 0):
                 print("Saldo inválido!")
            else:
                 self.__saldo = valor
    def gerar_saldo(self):
         print(f"Conta: {self.__numero}")
         print(f"Saldo: R${self.__saldo:10.2f}")