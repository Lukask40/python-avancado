lista = []

while True:
    nomes = input("Digite um nome: ")
    if (nomes != "fim"):
        lista. append(nomes)
    else :
        break

lista.sort()
print(lista)
print(len(lista))