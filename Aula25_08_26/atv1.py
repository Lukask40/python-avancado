
positivos = []
negativos = []
soma_positivos = 0


for i in range(10):
    num= float(input(f"Digite o {i + 1}º número: "))
    

    if num > 0:
        positivos.append(num)
        soma_positivos += num
    elif num < 0:
        negativos.append(num)

print("\nQuantidade de números positivos:", len(positivos))
print("Quantidade de números negativos:", len(negativos))
print("Vetor com os números negativos:", negativos)
print("Soma dos números positivos:", soma_positivos)
