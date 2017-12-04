import time

lista = list(range(5, 10000, 5))
num = int(input("Informe um valor: "))
qtde1 = 0
qtde2 = 0
qtde3 = 0
inicio = 0
fim = len(lista) - 1
repeticoes = 10000


# Busca sequencial simples
antes = time.time()
for i in range(repeticoes):
    for j in range(len(lista)):
        qtde1 += 1
        if (num == lista[j]):
            break
        
depois = time.time()

print("Tempo 1: ", (depois - antes))

if (j < len(lista) - 1):
    print("achei!!")
elif (lista[j] == num):
    print("achei")
else:
    print("nao achei")

print("Quantidade = ", qtde1)







# Busca sequencial - ordenada

antes = time.time()

for i in range(repeticoes):
    for j in range(len(lista)):
        qtde2 += 1
        if (num <= lista[j]):
            break
depois = time.time()

print("Tempo 2: ", (depois - antes))

if (num != lista[j]):
    print("nao achei")
else:
    print("achei")


# Busca binaria

antes = time.time()
for i in range(repeticoes):   
    meio = int((fim + inicio)/2)

    while ((fim > inicio) and (lista[meio] != num)):
        qtde3 += 1
        if (lista[meio] < num):
            inicio = meio + 1
        else:
            fim = meio - 1
        meio = int((fim + inicio)/2)

depois = time.time()

print("Tempo 3: ", (depois - antes))
if (lista[meio] == num):
    print("achei")
else:
    print("nao achei")


# analisando as três soluções
print(num)
print(qtde1)
print(qtde2)
print(qtde3)
