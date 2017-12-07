#menor valor

lista = [12, 3, 10, 7, 1, 5]

menor = lista[0]
indice_menor = 0

for i in range(len(lista)):
    if (lista[i] < menor):
        menor = lista[i]
        indice_menor = i

print(menor)
print(indice_menor)
