lista = ['', '', '']
matriz = [['', '', ''], ['', '', ''], ['', '', '']]

print(lista)
print(matriz)

matriz[1][1] = 'X'
matriz[2][2] = 'O'
matriz[1][2] = 'X'
matriz[1][0] = 'O'
matriz[2][0] = 'X'
matriz[0][0] = 'O'
matriz[0][2] = 'X'

print(matriz)
print(matriz[0])

for i in range(len(matriz)):
    for j in range(len(matriz[i])):
        if (matriz[i][j] == ""):
            print(" ", end = "")
        else:
            print(matriz[i][j], end = "")
    print()


# linhas e colunas
for i in range(len(matriz)):
    for j in range(len(matriz[i])):
        print(i, j)

print()

# colunas e linhas
for i in range(len(matriz)):
    for j in range(len(matriz[i])):
        print(j,i)

# zerando a matriz
for i in range(len(matriz)):
    for j in range(len(matriz[i])):
        matriz[i][j] = ""

print()

# diagonal principal
for i in range(len(matriz)):
    print(i,i)

print(matriz)
