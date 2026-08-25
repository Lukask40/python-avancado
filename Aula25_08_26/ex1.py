
temperatura = []

for x in range(5):
    temp=float(input(f"Digite a {x+1}ª temeperatura:  "))
    temperatura.append(temp)
    
media = sum(temperatura)/len(temperatura)
maior = max(temperatura)
menor = min(temperatura)

print(f"A media é: {media}")
print(f"A menor temperatura é: {menor}° e a maior é: {maior}°")