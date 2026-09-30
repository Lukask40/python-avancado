import customtkinter as ctk
ctk.set_appearance_mode("dark")


def calcular():
    nota1_aluno= float(nota1.get())
    nota2_aluno = float(nota2.get())
    nota3_aluno = float(nota3.get())
    
    try:
        nota_media = (nota1_aluno + nota2_aluno + nota3_aluno)/3

        if nota_media >= 5.0:
            resultado.configure(text=f"Sua nota foi {nota_media:.2f} , você foi aprovado")
            resultado.configure(fg_color="green")
        else:
            resultado.configure(text=f"Sua nota foi {nota_media:.2f} , você foi reprovado")
            resultado.configure(fg_color="red")
    except:
        resultado.configure(text="Por favor digite uma nota válida")
        resultado.configure(fg_color="red")








janela = ctk.CTk()
janela.geometry("600x600")
janela.resizable(False, False)
janela.title("Sistema escolar")
janela.iconbitmap("aula_30_09_26/ic_school_128_28729.ico")



titulo = ctk.CTkLabel(janela,
text="Sistema de nota",
text_color="yellow",
font=("Verdana", 50,))
titulo.pack()



nota1 = ctk.CTkEntry(janela,
                    width=400,
                    height=50,
                    border_color="yellow",
                    placeholder_text="Digite a nota da primeira unidade",
                    )
nota1.pack(pady=35)



nota2= ctk.CTkEntry(janela,
                    width=400,
                    height=50,
                    border_color="yellow",
                    placeholder_text="Digite a nota da segunda unidade",
                    
                    )
nota2.pack()

nota3 = ctk.CTkEntry(janela,
                    width=400,
                    height=50,
                    border_color="yellow",
                    placeholder_text="Digite a nota da terceira unidade",
                    
                    )
nota3.pack(pady=35)




botao = ctk.CTkButton(janela,
                    width=200,
                    height=40,
                        text="Calcular",
                        fg_color="yellow",
                        text_color="black",
                        cursor ="shuttle",
                        font=("Arial", 30),
                        command=calcular,
                        hover_color="DarkOrange",
                        
                        )

botao.pack(pady=35)


resultado =ctk.CTkLabel(janela,
                    text="",
                    text_color="white",
                    font=("Arial", 20))

resultado.pack()
                        


janela.mainloop()
