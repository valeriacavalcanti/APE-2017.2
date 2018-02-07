def maior_valor(lista):
    "Retorna o maior valor da lista"
    maior = lista[0]
    for i in range(len(lista)):
        if (lista[i] > maior):
            maior = lista[i]
    return maior

def menor_valor(lista):
    "Retorna o menor valor da lista"
    menor = lista[0]
    for i in range(len(lista)):
        if (lista[i] < menor):
            menor = lista[i]
    return menor
    
def media(lista):
    "Retorna a média dos valores da lista"
    soma = 0
    for i in range(len(lista)):
        soma += lista[i]
    return soma/len(lista)

def maior_menor(lista):
    "Retorna o maior e menor valor da lista"
    return maior_valor(lista), menor_valor(lista)

# verificar se existe problema
# dever de casa
def maior_menor_2(lista):
    "Retorna o maior e menor valor da lista - 2.0v"
    maior = lista[0]
    menor = lista[0]
    for i in range(len(lista)):
        if (lista[i] > maior):
            maior = lista[i]
        elif (lista[i] < menor):
            menor = lista[i]
    return maior, menor








    

    
