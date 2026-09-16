import customtkinter as ctk
ctk.set_appearance_mode("dark")


def calcular():
    distancia_km = float(distancia.get())
    consumo_km = float(consumo.get())
    preco_gasolina = float(preco_gasolina.get())

    litros_necessarios = distancia_km / consumo_km
    custo_total = litros_necessarios * preco_gasolina

    resultado.configure(text=f"Você precisará de {litros_necessarios:.2f} litros de gasolina.\nO custo total da viagem será de R${custo_total:.2f}.")









janela = ctk.CTk()
janela.geometry("600x600")
janela.resizable(False, False)
janela.title("CALCULADORA DE VIAGEM")
janela.iconbitmap("aula_16_09_26/travel-holiday-vacation-303_89062.ico")



titulo = ctk.CTkLabel(janela,
text="APP VIAGEM",
text_color="LightGray",
font=("Verdana", 50))
titulo.pack()



distancia = ctk.CTkEntry(janela,
                    width=400,
                    height=50,
                    border_color="LightGray",
                    placeholder_text="Digite a distancia da viagem em km",
                    )
distancia.pack(pady=35)



consumo = ctk.CTkEntry(janela,
                    width=400,
                    height=50,
                    border_color="LightGray",
                    placeholder_text="Digite o consumo do veiculo em km/l",
                    
                    )
consumo.pack()

preco_gasolina = ctk.CTkEntry(janela,
                    width=400,
                    height=50,
                    border_color="LightGray",
                    placeholder_text="Digite o preço atual da gasolina em R$",
                    
                    )
preco_gasolina.pack(pady=35)




botao = ctk.CTkButton(janela,
                    width=200,
                    height=40,
                        text="Calcular",
                        fg_color="LightGray",
                        text_color="black",
                        cursor ="shuttle",
                        font=("Arial", 30),
                        command=calcular
                        )

botao.pack(pady=35)


resultado =ctk.CTkLabel(janela,
                    text="",
                    text_color="white",
                    font=("Arial", 20))

resultado.pack()
                        


janela.mainloop()

