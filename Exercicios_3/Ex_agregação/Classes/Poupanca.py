class Poupanca:
    def __init__(self, taxa_remuneracao):
        self.__taxa_remuneracao = taxa_remuneracao

    def remuneraConta(self):
        self.__saldo += self.__saldo * self.__taxa_remuneracao