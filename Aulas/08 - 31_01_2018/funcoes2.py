def nome_lindo():
    print("Vou te mostrar um nome lindo")
    for i in range(10):
        print("Valéria")

def matricula_ape_2018_1():
    print("viviane"*4)
    print("janaina")
    print("mateus")
    print("")

def somar(n1, n2):
    resultado = n1 + n2
    return resultado

def super_somar(*num):
    soma = 0
    for n in num:
        soma += n
    return soma

def maior(num1, num2 = 10):
    if (num1 > num2):
        return num1
    else:
        return num2

def pessoa_mara_hum():
    return "Valéria",15

def add(num):
    num += 1
    print("num =", num)

def inserir(lista, num):
    lista.append(num)

#desafio para você descobrir
def super_add():
    numero += 2
    

# programa começa aqui!

nome_lindo()
print(somar(10,20))
print(somar(5,10)*2)
#print(pessoa_mara_hum())
nome, idade = pessoa_mara_hum()
print(nome, idade)
#print(n1)
#print(resultado)

print(super_somar(10,20))
print(super_somar(10,20, 30, 40, 50))
print(super_somar(10,20, 30, 40, 50, 60, 70, 80))
print(maior(5,7))
print(maior(5))
print(maior(num1 = 5, num2 = 7))

# variável do programinha
numero = 10
add(numero)
print("numero = ", numero)

super_add()



numeros = [1,2,3,4,5,6]
inserir(numeros, 7)
print(numeros)

# programa termina aqui!


