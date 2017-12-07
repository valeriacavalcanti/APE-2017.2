# ordenação: Algoritmo da Bolha

# lista = [12, 4, 5, 2]
# lista = [2, 4, 5, 8]
# lista = [5, 4, 3, 2]
# lista = [4, 2, 5, 8]
lista = [2, 2, 2, 2]

qt_troca = 0
qt_for = 0

esta_ordenada = False

while (esta_ordenada == False):
    esta_ordenada = True

    qt_for += 1
    for i in range(len(lista) - 1):        
        if (lista[i] > lista[i + 1]):
            qt_troca += 1
            esta_ordenada = False
            aux = lista[i]
            lista[i] = lista[i + 1]
            lista[i + 1] = aux

print(lista)
print(qt_troca)
print(qt_for)
