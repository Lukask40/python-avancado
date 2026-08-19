
# for x in range(61):
#     if  (x % 2 == 0):
#         print(x)
    


# while True:
#     for x in range(61):
#         if  (x % 2 == 0):
#             print(x)
            
    

carrinho = []

while True:
    produto = float(input("Digite o valor do produto: "))
    if(produto == 0):
        break
    else:
        carrinho.append(produto)
        
total = sum(carrinho )
print(f" O valor total é : {total}")