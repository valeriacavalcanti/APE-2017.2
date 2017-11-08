h=1
n=int(input("Digite um numero: "))
for i in range (1,n+1):
  if (i%2!=0):
    h=h-(1/(2*i))
  else:
    h=h+(1/(2*i))
print("soma = ", h)