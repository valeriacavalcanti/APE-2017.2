import funcoes
import random
#Sexta questão

#numeros = [1,2,3,4,5,6,7,8,9,10]
#numeros = [10,9,8,7,6,5,4,3,2,1]
numeros = []

for i in range(10):
    numeros.append(random.randint(1,100))

print(numeros)

print(funcoes.maior_valor(numeros))
print(funcoes.menor_valor(numeros))
print(funcoes.media(numeros))
print(funcoes.maior_menor(numeros))
print(funcoes.maior_menor_2(numeros))
