
import customtkinter as ctk
import qrcode
from PIL import ImageTk

ctk.set_appearance_mode("dark")

janela = ctk.CTk()
janela.geometry("400x500")
janela.title("Sistema Gerador de QR CODE")
janela.resizable(False, False)

imagem_qr = None


def gerar_qr():
    global imagem_qr

    texto = entrada.get().strip()

    if texto:
        qr = qrcode.make(texto)
        qr = qr.resize((250, 250))

        imagem_qr = ImageTk.PhotoImage(qr)
        resultado.configure(image=imagem_qr, text="")
    else:
        resultado.configure(
            image=None,
            text="Digite o texto para gerar o QR Code"
        )


titulo = ctk.CTkLabel(
    janela,
    text="Sistema Gerador de QR Code",
    text_color="yellow",
    font=("Arial", 24, "bold")
)
titulo.pack(pady=15)

entrada = ctk.CTkEntry(
    janela,
    placeholder_text="Digite o texto para gerar o QR Code",
    width=300,
    height=50,
    corner_radius=10,
    border_width=2,
    border_color="yellow",
    font=("Arial", 15)
)
entrada.pack(pady=10)

botao = ctk.CTkButton(
    janela,
    text="Gerar QR Code",
    command=gerar_qr,
    width=200,
    height=40,
    corner_radius=10,
    border_width=2,
    border_color="yellow",
    font=("Arial", 15),
    fg_color="orange",
    hover_color="silver",
    text_color="black",
    cursor="hand2"
)
botao.pack(pady=10)

resultado = ctk.CTkLabel(janela, text="")
resultado.pack(pady=15)

janela.mainloop()
