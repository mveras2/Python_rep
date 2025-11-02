#Torre de Hanoi

def mov_disco(origem, destino):
    disco = origem.pop()     #função pop remove e retorna um elemento de uma lista. Se não declarar ninguém vai retirar o último
    destino.append (disco)   #função append: adiciona um único elemento ao final de uma lista


def imprimir_torres(torre_A, torre_B, torre_C):
    print("A:", torre_A)
    print("B:", torre_B)
    print("C:", torre_C)
    print()

def torre_hanoi(num_discos, origem, destino, aux):
    if num_discos == 1:
        mov_disco(origem, destino)
        imprimir_torres(torre_A, torre_B, torre_C)
    else: 
        torre_hanoi(num_discos - 1, origem, aux, destino)
        mov_disco(origem, destino)
        imprimir_torres(torre_A, torre_B, torre_C)
        torre_hanoi(num_discos - 1, aux, destino, origem)

#Chamada do programa
num_discos = 10
#inicializando as torres
torre_A = list(range(num_discos, 0, -1))
torre_B = []
torre_C = []
#Estado inicial
imprimir_torres(torre_A, torre_B, torre_C)
torre_hanoi(num_discos, torre_A, torre_C, torre_B)
