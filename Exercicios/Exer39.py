#Exercício 39 - Leitura de data de nascimento
#importar a biblioteca
from datetime import datetime

#recebe a data
data = input('Insira a sua data de nascimento [dd/mm/aaaa]:')

#trata a data
try: 
    data_str = datetime.strptime(data, "%d/%m/%Y")
    #print(f"A data lida é: {data_str}")
    #print(f"Dia: {data_str.day}, Mês: {data_str.month}, Ano:{data_str.year}")
    ano_nasc = data_str.strftime('%Y')
    print("O ano de nascimento é:", ano_nasc)

    #coleta a data atual
    data_ag = datetime.now()
    ano_atual = data_ag.strftime('%Y')
    print("O ano atual é:", ano_atual)

    aux = int(ano_atual)-int(ano_nasc)

    #Comparação do alistamento
    if aux >= 18:
        print('Você já passou do período de alistamento. Procure a junta militar para regularização')
    elif aux >=17 and aux<18:
        print('Você está no período regular de alistamento, procure uma junta militar.')
    else:
        print('Você ainda não tem idade para se alistar')

except ValueError:   
    print("Formato inválido")

