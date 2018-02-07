import random

"""
lista = [5, 4, 19, 27, 41, 32, 16]

num = random.randint(1,60)
print (num)

print(random.choice(lista))
"""

aposta = []

for i in range(6):
    aposta.append(random.randint(1, 60))

print(aposta)
