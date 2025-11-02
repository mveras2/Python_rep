#Programa que valida o CPF
#função para validar o CPF
def valida_cpf(num_cpf):
#valida o numero de digitos inteiros
    if len(num_cpf) != 11:
        return False
#valida se os valores não são iguais
    for i in range(10):
        if num_cpf[i] != num_cpf[i+1]:
            continue
        elif i == 9:
            return False
        else: continue
    
    
    #result = sum(int(num_cpf[i]) for i in range(11))
    #for valor in num_cpf:
    #    result += num_cpf[valor]
    #if result == num_cpf[0]*11:
    #    return False

#Calculo do primeiro verificador
# regra: O primeiro passo é calcular o primeiro dígito verificador, e para isso, separamos os primeiros 9 
# dígitos do CPF (111.444.777) e multiplicamos cada um dos números, da direita para a esquerda por números 
# crescentes a partir do número 2, como no exemplo abaixo:
   
    soma = sum(int(num_cpf[i])*(10-i) for i in range(9))  

#Pegamos o resultado obtido 162 e dividimos por 11.  Consideramos como quociente apenas o valor inteiro. 
    resto = soma % 11
#- Se o resto da divisão for menor que 2, então o dígito é igual a 0 (Zero).
#- Se o resto da divisão for maior ou igual a 2, então o dígito verificador é igual a 11 menos o resto da divisão (11 - resto).
    if int(resto) < 2:
        verif1 = 0
    else: verif1 = 11-int(resto)

    if verif1 != int(num_cpf[-2]):
        return False           

#Cálculo do segundo dígito verificador
# segue a mesma lógica só que agora insero o primeiro digito verificador na conta
    soma = sum(int(num_cpf[i])*(11-i) for i in range(10))  
   # for i in range(10): 
   #     soma = sum(int(cpf[i]))*(11-i)  
#Dividimos o total do somatório por 11 e consideramos o resto da divisão.    
    resto=soma % 11
#Após obter o resto da divisão, precisamos aplicar a mesma regra que utilizamos para obter o primeiro dígito:
    if int(resto) < 2:
        verif2 = 0
    else: verif2 = 11-int(resto)

    if verif2 != int(num_cpf[-1]):
        return False     
    return True

# codigo de entrada do CPF e chamada da função de vaidação

cpf = input("Digite o CPF para validação:")
vec_cpf = list(cpf)  #insere cada um dos caracteres no vetor
num_cpf=[]   #é previso criar uma lista para inserir os valores

for val in vec_cpf:    
    if val.isdigit() == True:
        #print(val)
        num_cpf.append(int(val))
        #a+=1

#print(f"Os valores munéricos do CFP digitado foram: {num_cpf}")
if valida_cpf(num_cpf) == False:
    print("Esse CPF é INválido.")
else: print("O CPF é Válido.")
#print(f"O CFP possui {a} digitos inteiros")


#Começar as validações dos valores

