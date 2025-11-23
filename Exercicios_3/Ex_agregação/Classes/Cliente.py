class Cliente:
    
    def __init__(self, cpf, nome, endereco):
        self.__cpf = cpf
        self.__nome = nome
        self.__endereco = endereco

# quando inseri as classes privadas, para garantir a funcionalidade tem que criar o seguinte
# código para que os atributos sejam manipulados corretamente entre os objetos

    def get_cpf(self):
        return self.__cpf

    def get_nome(self):
        return self.__nome

    def get_endereco(self):
        return self.__endereco    