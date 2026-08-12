# revisao variaveis

# nome = "Laiane"
# sal_bruto = 8789.18
# ir = sal_bruto * 0.18
# inss = sal_bruto * 0.05
# sal_liquido = sal_bruto - ir - inss

# print(f'Sr(a) {nome} o seu salario liquido é R$ {sal_liquido:.2f}')

uni1 = float(input('Digite sua nota da 1ª unidade:'))
uni2 = float(input('Digite sua nota da 2ª unidade:'))
uni3 = float(input('Digite sua nota da 3ª unidade:'))

media = (uni1 + uni2+ uni3) / 3

if (media>= 7):
    print(f"A sua média é {media:.1f} - você foi aprovado")
else:
    print(f"A sua média é {media:.1f} - você foi reprovado")