# Atividade 4
numeros = []
while True:
    num =int(input("Digite um número: "))
    if (num!=0):
        numeros.append(num)
    else:
        break

soma = sum(numeros)
print(f"A soma é: {soma}")