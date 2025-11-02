import datetime
from Classes.Extrato import Extrato


class Conta1: # Essa classe foi copiada do aqrquivo anterior, porém com alterações para se adequer a esse exercício

    def __init__(self, clientes, numero, saldo):    # a função def __init__ é chamada de construtor
        self.clientes = clientes
        self.numero = numero
        self.saldo = saldo
        self.data_abertura = datetime.datetime.today()
        self.extrato = Extrato()

    def depositar(self, valor):      # Novo método da classe - a função def cria um método. O Construtor é um método
        self.saldo = self.saldo + valor  # pode-se usar também : self.saldo += valor
        self.extrato.transacoes.append(["Depósito", valor, datetime.datetime.today()])

    def sacar(self, valor):
        #para o saldo precisamos usar uma verificação de saldo válido
        if self.saldo < valor:
                return False # Não tem saldo suficiente
        else: 
             self.saldo -= valor
             self.extrato.transacoes.append(["Saque", valor, datetime.datetime.today()])  
             return True # Saque realizado com sucesso
    
    #def gerar_extrato(self):
    #    print(f"Nome do titular: {self.nome}\nNúmero da conta: {self.numero}\nCPF do titulara: {self.cpf}\nSaldo da conta: R${self.saldo}")
        
    def transfere_valor(self, conta_destino, valor):
        if self.saldo < valor:
             return("Não existe saldo suficiente")
        else:
             conta_destino.depositar(valor)
             self.saldo -= valor
             self.extrato.transacoes.append(["Trasferência", valor, datetime.datetime.today()])  
             return("Transferência Realizada")

    def gerar_saldo(self):
         print(f"Conta: {self.numero}")
         print(f"Saldo: R${self.saldo:10.2f}")