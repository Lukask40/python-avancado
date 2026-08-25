notas = []

for x in range(8):
    nota=float(input(f"Digite a {x+1}ª nota:  "))
    notas.append(nota)
    
media = sum(notas)/len(notas)

print(f"A media é: {media:.2f}")

notas_acima_da_media = [n for n in notas if n > media]


print(f"Notas acima da média: {notas_acima_da_media:.2f}")