# Ordenação: seleção direta

lista = [12, 8, 16, 5]

for i in range(len(lista) - 1):
    #print ("[",i, "]")
    # descobrir o índice com o menor valor
    indice_menor = i
    for j in range(i, len(lista)):
        if (lista[j] < lista[indice_menor]):
            indice_menor = j
    if (i != indice_menor):
        aux = lista[i]
        lista[i] = lista[indice_menor]
        lista[indice_menor] = aux

print(lista)
