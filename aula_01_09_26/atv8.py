
notas = []


while True:
    nota = float(input("Digite uma nota (ou -1 para encerrar): "))
    
    if nota == -1:
        break
        
    notas.append(nota)


if len(notas) > 0:
    print("\n--- Notas Cadastradas ---")
    
    for n in notas:
        print(f"Nota: {n}")

    
    quantidade = len(notas)
    media = sum(notas) / quantidade
    maior_nota = max(notas)
    menor_nota = min(notas)


    notas.sort()
    notas.reverse()

    
    print("\n--- Resumo dos Dados ---")
    print(f"Quantidade de notas: {quantidade}")
    print(f"Média das notas: {media:.2f}")
    print(f"Maior nota: {maior_nota}")
    print(f"Menor nota: {menor_nota}")
    print(f"Notas em ordem decrescente: {notas}")
else:
    print("Nenhuma nota foi cadastrada.")
