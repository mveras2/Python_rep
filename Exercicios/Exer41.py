from datetime import datetime

#recebe a data
data = input('Insira a sua data de nascimento [dd/mm/aaaa]:')

#trata a data
try:   
    data_str = datetime.strptime(data, "%d/%m/%Y")
    ano_nasc = data_str.strftime('%Y')
   
    #coleta a data atual
    data_ag = datetime.now()
    ano_atual = data_ag.strftime('%Y')

    #Comparador
    aux = int(ano_atual)-int(ano_nasc)
    
    if aux >= 20:
        print("Sua categoria é MASTER.")
    elif aux >= 19:
        print("Sua categoria é SÊNIOR.")
    elif aux >= 14:
        print("Sua categoria é JUNIOR")
    elif aux >= 9:
        print("Sua categoria é INFANTIL")
    else:
        print("Sua categoria é MIRIM")
    
except ValueError:   
    print("Formato inválido")