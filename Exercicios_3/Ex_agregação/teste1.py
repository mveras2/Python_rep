# Testando o código
from Classes.Cliente import Cliente
from Classes.Conta1 import Conta1

# Recomenda-se manter duas linhas de separação entre a importação e o código principal
cliente1 = Cliente("123", "João", "Rua X")
cliente2 = Cliente("224", "Maria", "Rua Y")

conta_1 = Conta1([cliente1, cliente2], 111, 0)

conta_1.depositar(1000)
conta_1.sacar(200)
conta_1.sacar(150)
conta_1.depositar(2000)
conta_1.sacar(1000)
conta_1.extrato.gerar_extrato(conta_1.numero)
conta_1.gerar_saldo()
