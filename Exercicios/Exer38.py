#Exercício 38

print('Esse exercício compara dois valores:')
valor1 = float(input('insira o primeiro valor:'))
valor2 = float(input('insira o segundo valor:'))
#compara os valores

if valor1 == valor2:
    print('Os valores são iguais.')
elif valor1 > valor2:
    print('O primeiro valor é maior que o segundo.')
else:
    print('O segundo valor é maior que o primeiro.')
