lista = []

for i in range(4):
    num = int(input("Informe um número: "))
    lista.append(num)

print(lista)

troca = True
while (troca):
    troca = False
    for i in range(len(lista) - 1):
        if (lista[i] > lista[i + 1]):
            lista[i], lista[i + 1] = lista[i + 1], lista[i]
            troca = True

print(lista)

lista.append(int(input("Informe um valor: ")))
lista.append(int(input("Informe um valor: ")))

print(lista)

troca = True
while (troca):
    troca = False
    for i in range(len(lista) - 1):
        if (lista[i] > lista[i + 1]):
            lista[i], lista[i + 1] = lista[i + 1], lista[i]
            troca = True

print(lista)
