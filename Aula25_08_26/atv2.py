import random, os
nomes = []



for i in range(10):
    nome = input(f"Digite o {i + 1}º nome: ")
    nomes.append(nome)
    os.system('cls' or 'clear')
    
    
sorteado = random.choice(nomes)

print(f"\nO nome sorteado é: {sorteado}")


