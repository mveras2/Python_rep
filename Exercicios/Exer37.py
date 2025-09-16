#Exercício 37
valor = int(input('Insira um valor inteiro qualquer:'))

aux = input('Escolha o padrão de consersão desejado (bin, oct, hexa): ')

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
