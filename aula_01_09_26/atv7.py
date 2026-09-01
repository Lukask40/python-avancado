import random


numero_secreto = random.randint(1, 20)
tentativas = 0

print("🔢 Bem-vindo ao jogo de adivinhação! Tente adivinhar o número entre 1 e 20.")

while True:
    
    palpite = int(input("\nDigite o seu palpite: "))
    tentativas += 1

    
    if palpite == numero_secreto:
        print(f" Parabéns! Você acertou em {tentativas} tentativas.")
        break 
    elif palpite < numero_secreto:
        print("📈 Errou! O número secreto é MAIOR.")
    else:
        print("📉 Errou! O número secreto é MENOR.")
