
senha = input("Digite uma senha de 4 dígitos numéricos: ")


while len(senha) != 4 or not senha.isdigit():
    print("Senha Inválida")
    senha = input("Digite uma senha de 4 dígitos numéricos: ")


print("Senha cadastrada com sucesso")
