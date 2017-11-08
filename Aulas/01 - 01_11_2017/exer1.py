"""
	valor < 100 - 1 parcela
	100 <= valor < 200 - 2 parcelas
	200 <= valor < 400 - 3 parcelas
	400 <= valor < 600 - 4 parcelas
	>= 600 - 5 parcelas
"""

valor = float(input("Informe o valor: "))

if (valor < 100):
	print("1 parcela de", valor)
else:
	if (valor < 200):
		print("2 parcelas de", valor/2)
	else:
		if (valor < 400):
			print("3 parcelas de", valor/3)
		else:
			if (valor < 600):
				print("4 parcelas de", valor/4)
			else:
				print("5 parcelas de", valor/5)
print("que bom !")