import customtkinter as ctk
ctk.set_appearance_mode("dark")

janela = ctk.CTk()
janela.geometry("500x350")
janela.resizable(False, False)
janela.title("Sistema de acesso-2026")
janela.iconbitmap("aula_15_09_26/login_gov_icon_146024.ico")



titulo = ctk.CTkLabel(janela,
text="Sistema de Login",
text_color="#09A3F0",
font=("Arial", 50))
titulo.pack()



login = ctk.CTkEntry(janela,
                    width=400,
                    height=50,
                    border_color="#09A3F0",
                    placeholder_text="Digite seu login",
                    )
login.pack(pady=35)



senha= ctk.CTkEntry(janela,
                    width=400,
                    height=50,
                    border_color="#09A3F0",
                    placeholder_text="Digite sua senha",
                    show="•"
                    )
senha.pack()

botao = ctk.CTkButton(janela,
                    width=200,
                    height=40,
                        text="Entrar",
                        fg_color="#09A3F0",
                        text_color="black",
                        cursor ="shuttle",
                        font=("Arial", 30)
                        )

botao.pack(pady=35)
                        


janela.mainloop()


