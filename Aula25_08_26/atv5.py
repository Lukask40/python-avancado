
import os
import time
senha = input("Digite uma senha de 4 dígitos numéricos: ")



while len(senha) != 4 or not senha.isdigit():
    print("Senha Inválida")
    time.sleep(3)
    os.system('cls' or 'clear')
    senha = input("Digite uma senha de 4 dígitos numéricos: ")


print("Senha cadastrada com sucesso")
