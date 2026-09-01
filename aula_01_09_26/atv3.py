
numeros = []

for x in range(5):
    num=float(input(f"Digite o {x+1}ª número:  "))
    numeros.append(num)
    
soma = sum(numeros)
maior = max(numeros)
menor = min(numeros)

print(f"A soma é: {soma}")
print(f"A menor numero é: {menor}° e a maior é: {maior}°")
numeros.sort()
print(numeros)