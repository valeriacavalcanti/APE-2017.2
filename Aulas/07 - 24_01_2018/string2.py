frase = ""

palavra = input("Informe uma palavra: ")
while (palavra.upper() != "FIM"):
    frase += palavra + " "
    palavra = input("Informe uma palavra: ")

print(frase)
