nota1=float(input("Nota da primeira prova:"))
nota2=float(input("Nota da segunda prova:"))

media = (nota1+nota2)/2

if media < 5:
    print("Você reprovou.")
elif media >=5 and media < 6.9:
    print("Você está de recuperação.")
else:
    print("Você está aprovado")

