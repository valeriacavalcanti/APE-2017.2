base=int(input("Digite base: "))
expoente=int(input("Digite expoente: "))
#print("resultado = ", base**expoente)
potencia=1
for i in range (0,expoente):
  potencia=potencia*base
print("Potencia=",potencia)
  
  