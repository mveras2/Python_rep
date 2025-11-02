#Exercício 37
valor = int(input('Insira um valor inteiro qualquer:'))

aux = input('Escolha o padrão de consersão desejado (bin, oct, hexa): ')

#uma outra forma de escolha de objetos usando python é com a utilização de '''. Com esse artifício é posivel montar um estrutura parecida com o swicth
#print(''' Escolha uma das bases oara converção:
#            [1] converter para binário
#            [2] converter para octal
#            [3] converter para Hexadecimal''')

if aux == 'bin' or aux == 'BIN'or aux == 'oct' or aux == 'OCT' or aux == 'hexa' or aux == 'HEXA':
    if aux == 'bin' or aux == 'BIN':
        valor = bin(valor)[2:]
    elif aux == 'oct' or aux == 'OCT':
        valor = oct(valor)[2:]
    elif aux == 'hexa' or aux == 'HEXA':
        valor = hex(valor)[2:]
else:
    print('Padrão inválido. Tente novamente.')
            
print(valor)
