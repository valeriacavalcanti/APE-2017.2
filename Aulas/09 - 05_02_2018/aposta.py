import random

# funções

def inserir(lista, num):
    "Tentar inserir um numero na lista."
    if (num not in lista):
        lista.append(num)
        return True
    else:
        return False


def gerar_sorteio(lista):
    "Gerar seis número aleatórios e distintos"
    while(len(lista) < 6):
        inserir(lista, random.randint(1, 60))


# programa principal

aposta = []
sorteio = []
"""
while (len(aposta) < 6):
    numero = int(input("Informe um número:"))
    if (inserir(aposta, numero) == False):
        print("Erro: Número duplicado")

print(aposta)

gerar_sorteio(sorteio)
print(sorteio)
"""
print(gerar_sorteio.__main__)

