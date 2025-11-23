# Testando o código
from Classes.Cliente import Cliente
from Classes.Conta1 import Conta1
from Classes.ContaEspecial import ContaEspecial
from Classes.ContaRemunerada import ContaRemuneradaPoupanca


# Recomenda-se manter duas linhas de separação entre a importação e o código principal
cliente1 = Cliente("123", "João", "Rua X")
cliente2 = Cliente("224", "Maria", "Rua Y")
cliente3 = Cliente("567", "Zé", "Rua Z")

#conta_1 = Conta1([cliente1, cliente2], 111, 0)
conta_1 = Conta1(cliente1, 111, 3000)
conta_2 = Conta1(cliente2, 111, 2000)
conta_3 = ContaEspecial(cliente3, 113, 2000, 1000)
conta_4 = ContaRemuneradaPoupanca(cliente3, 3, 2000, 0.1)

conta_4.remuneraConta()
conta_4.gerar_saldo()
conta_2.depositar(800)
conta_2.gerar_extrato()


#conta_1.gerar_saldo()
#conta_2.gerar_saldo()
#conta_3.gerar_saldo()



#conta_1.depositar(300)
#conta_1.transfere_valor(conta_2, 500)
#conta_2.sacar(700)
#conta_3.depositar(800)
#conta_3.sacar(4000)

#conta_1.gerar_extrato()
#conta_2.gerar_extrato()
#conta_3.gerar_extrato()

#conta_1.sacar(150)
#conta_1.depositar(2000)
#conta_1.sacar(1500)

#conta_1.gerar_extrato()
#conta_1.gerar_saldo()