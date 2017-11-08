qtde = 0
soma = 0
n = int(input("Informe um valor: "))

while (n != 0):
	print("[", n, "]")
	# qtde = qtde + 1
	qtde += 1
	# soma = soma + n
	soma += n
	n = int(input("Informe um valor: "))

print("quantidade =", qtde)
print("soma =", soma)