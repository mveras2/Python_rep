# aula sobre bibliotecas

# import math --- biblioteca de funções matemáticas
# exemplo de uso de uma função da biblioteca
# raiz = (-b + math.sqrt(delta))/ (2*a)



# Projeto do Tema 4 com o uso da biblioteca tkinter
#no git o programa não gera as janelas, porém no console está funcionando

import tkinter as tk
from tkinter import messagebox

def somanumero():
    num1 = float(entry_num1.get())
    num2 = float(entry_num2.get())
    soma = num1 + num2
    messagebox.showinfo("resultado", f"A soma dis números é: {soma}")


#criando a janela

janela = tk.Tk()
janela.title("Calculadora de Soma")

#Criando os widgets
label_num1 = tk.Label(janela, text="Número 1:")
label_num1.grid(row=0, column=0, padx=10, pady=5, sticky="e")

entry_num1 = tk.Entry(janela)
entry_num1.grid(row=0, column=1, padx=10, pady =5)

label_num2 = tk.Label(janela, text="Número 2:")
label_num2.grid(row=1, column=0, padx=10, pady=5, sticky="e")

entry_num2 = tk.Entry(janela)
entry_num2.grid(row=1, column=1, padx=10, pady =5)

botao_somar = tk.Button(janela, text="Somar", command=somanumero)
botao_somar.grid(row=2, column=2, padx=10, pady=5)

#Rodar o loop
janela.mainloop() #para deixar a janela disponível
