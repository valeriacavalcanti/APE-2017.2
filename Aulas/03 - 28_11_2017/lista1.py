qtde = 0
lista = [1,2,3,5,5,5,5,5,5,7,8]

numero = int(input("Informe um valor: "))

for i in range(len(lista)):
        if (lista[i] == numero):
                qtde += 1

print("Quantidade = ", qtde)
