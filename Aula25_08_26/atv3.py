nomes = []



for i in range(10):
    nome = input(f"Digite o {i + 1}º nome: ")
    nomes.append(nome)
    

ordem =nomes.sort()
for nome in nomes:
    print(nome)