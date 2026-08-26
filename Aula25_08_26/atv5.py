
import os
import time
senha = input("Digite uma senha de 4 dígitos numéricos: ")



while len(senha) != 4 or not senha.isdigit():
    print("Senha Inválida")
    time.sleep(3)
    os.system('cls' or 'clear')
    senha = input("Digite uma senha de 4 dígitos numéricos: ")


print("Senha cadastrada com sucesso")

#jeito do professor
# import os, time
# while True:
# senha = input('Cadastre a Senha: ')
# if(len(senha) == 4 and senha.isdigit()):
# print('Senha Cadastrada com Sucesso!')
# break
# else:
# print('Senha Invalida !!')
# time.sleep(3)
# os.system('cls' or 'clear')
