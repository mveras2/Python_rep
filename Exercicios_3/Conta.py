#Código da Classe
class Conta:                          # Chamada para criar classe - Utilizar a primeira letr em maiúsculo
    def __init__(self, numero, cpf, nomeTitular, saldo):    # a função def __init__ é chamada de construtor
        self.numero = numero
        self.cpf = cpf
        self.nomeTitular = nomeTitular
        self.saldo = saldo

    def depositar(self, valor):      # Novo método da classe - a função def cria um método. O Construtor é um método
        self.saldo = self.saldo + valor  # pode-se usar também : self.saldo += valor

    def sacar(self, valor):
        #para o saldo precisamos usar uma verificação de saldo válido
        if self.saldo < valor:
                return False # Não tem saldo suficiente
        else: 
             self.saldo -= valor
             return True # Saque realizado com sucesso
    
    def gerar_extrato(self):
        print(f"Nome do titular: {self.nomeTitular}\nNúmero da conta: {self.numero}\nCPF do titulara: {self.cpf}\nSaldo da conta: R${self.saldo}")
        
    def transfere_valor(self, contaDestino, valor):
        if self.saldo < valor:
             return("Não existe saldo suficiente")
        else:
             contaDestino.depositar(valor)
             self.saldo -= valor
             return("Transferência Realizada")


#Código do Exemplo
#____________________________________________________________________________
#criando um objeto ou Instanciando um objeto
#c1 = Conta( numero=1, cpf=12344321, nomeTitular="Guanabara", saldo=9000)
#c1.depositar(500)

#valor_saque = 300
#resultado_saque = c1.sacar(valor_saque)
#if resultado_saque:
#    print(f"Saque de R${valor_saque} realizado com sucesso!")
#else: 
#    print(f"Saldo insuficiente para realizar o saque!")
#___________________________________________________________________________
#c1.gerar_extrato()
#print(f"Nome do titular da conta: {c1.nomeTitular}")
#print(f"Numaro da conta: {c1.numero}")
#print(f"CPF do titular da conta: {c1.cpf}")
#print(f"Saldo da conta: R${c1.saldo}")
#_____________________________________________________________________________

conta1 = Conta( numero=123, cpf=8888888, nomeTitular="Maria", saldo=0)
conta2 = Conta( numero=124, cpf=9999999, nomeTitular="Pedro", saldo=500)
#______________________________________________________________________________
#if conta1 == conta2:
#     print("São iguais")
#else:
#     print("São diferentes")
#______________________________________________________________________________
print(conta2.transfere_valor(conta1, 300))

conta1.gerar_extrato()
conta2.gerar_extrato()
