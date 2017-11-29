qtde = 0
lista = [1,2,3,5,5,5,5,5,5,7,8]
i = 0

numero = int(input("Informe um valor: "))

while ((lista[i] <= numero) and (i < len(lista))):
       if (lista[i] == numero):
               qtde += 1
       i += 1

print("Quantidade = ", qtde)
