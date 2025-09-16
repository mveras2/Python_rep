#Exercício 36
#Entradas
print('Programa para validação de empréstimo bancário:')
print('Insira as seguintes informações:')
valor_casa = float(input('Valor da casa:'))
valor_sal = float(input('Valor do salário mensal:'))
tempo_fin = (input('Insira o tempo para o financiamento [em anos]:'))

#Estrutura de cácludo
prestacao = valor_casa / (int(tempo_fin)*12)

#saída
if prestacao > (valor_sal*0.3):
    print('Essa casa não pode ser financiada. O valor da prestação exece o limite de 30% do salário.')
else:
    print('Parabéns, sua compra foi aprovada!')

# teste
#print(f'{valor_casa:.2f}')
#print(f'{valor_sal:.2f}')
#print(f'{prestacao:.2f}')
#print(tempo_fin)