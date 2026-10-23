import customtkinter as ctk

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")


def calcular():
    try:
        nota1_aluno = float(nota1.get().replace(",", "."))
        nota2_aluno = float(nota2.get().replace(",", "."))
        nota3_aluno = float(nota3.get().replace(",", "."))

        notas = [nota1_aluno, nota2_aluno, nota3_aluno]

        if not all(0 <= nota <= 10 for nota in notas):
            resultado.configure(
                text="⚠️ As notas devem estar entre 0 e 10!",
                fg_color="#7F1D1D"
            )
            progresso.set(0)
            return

        nota_media = sum(notas) / 3
        progresso.set(nota_media / 10)

        if nota_media >= 7:
            mensagem = "🏆 APROVADO!"
            cor = "#065F46"
            detalhe = "Parabéns! Você mandou muito bem!"

        elif nota_media >= 5:
            mensagem = "⚡ RECUPERAÇÃO!"
            cor = "#92400E"
            detalhe = "Você está perto! Continue estudando."

        else:
            mensagem = "❌ REPROVADO"
            cor = "#991B1B"
            detalhe = "Não desista! Você pode melhorar."

        resultado.configure(
            text=f"{mensagem}\n\n"
                 f"Média final: {nota_media:.2f}\n"
                 f"{detalhe}",
            fg_color=cor
        )

    except ValueError:
        resultado.configure(
            text="⚠️ Digite números válidos nas três notas!",
            fg_color="#7F1D1D"
        )
        progresso.set(0)


def limpar():
    nota1.delete(0, "end")
    nota2.delete(0, "end")
    nota3.delete(0, "end")

    resultado.configure(
        text="Preencha as notas para começar!",
        fg_color="#24243A"
    )

    progresso.set(0)


janela = ctk.CTk()
janela.geometry("700x800")
janela.resizable(False, False)
janela.title("NEON SCHOOL | Sistema Acadêmico")
janela.configure(fg_color="#10101C")


titulo = ctk.CTkLabel(
    janela,
    text="⚡ NEON SCHOOL",
    text_color="#00E5FF",
    font=("Verdana", 35, "bold")
)
titulo.pack(pady=(25, 5))


subtitulo = ctk.CTkLabel(
    janela,
    text="SISTEMA INTELIGENTE DE DESEMPENHO",
    text_color="#A78BFA",
    font=("Arial", 14, "bold")
)
subtitulo.pack(pady=(0, 20))


painel = ctk.CTkFrame(
    janela,
    width=540,
    height=330,
    corner_radius=20,
    fg_color="#1A1A2E",
    border_width=2,
    border_color="#6C63FF"
)
painel.pack(pady=10, padx=30, fill="x")
painel.pack_propagate(False)


texto_painel = ctk.CTkLabel(
    painel,
    text="📚  BOLETIM DO ALUNO",
    font=("Arial", 22, "bold"),
    text_color="white"
)
texto_painel.pack(pady=(20, 15))


nota1 = ctk.CTkEntry(
    painel,
    width=420,
    height=45,
    corner_radius=12,
    border_color="#00E5FF",
    placeholder_text="Digite a nota da primeira unidade",
    font=("Arial", 15)
)
nota1.pack(pady=8)


nota2 = ctk.CTkEntry(
    painel,
    width=420,
    height=45,
    corner_radius=12,
    border_color="#00E5FF",
    placeholder_text="Digite a nota da segunda unidade",
    font=("Arial", 15)
)
nota2.pack(pady=8)


nota3 = ctk.CTkEntry(
    painel,
    width=420,
    height=45,
    corner_radius=12,
    border_color="#00E5FF",
    placeholder_text="Digite a nota da terceira unidade",
    font=("Arial", 15)
)
nota3.pack(pady=8)


botoes = ctk.CTkFrame(
    janela,
    fg_color="transparent"
)
botoes.pack(pady=20)


botao_calcular = ctk.CTkButton(
    botoes,
    width=220,
    height=50,
    text="🚀 CALCULAR MÉDIA",
    fg_color="#6C63FF",
    hover_color="#5148D7",
    text_color="white",
    font=("Arial", 16, "bold"),
    corner_radius=12,
    cursor="hand2",
    command=calcular
)
botao_calcular.pack(side="left", padx=8)


botao_limpar = ctk.CTkButton(
    botoes,
    width=130,
    height=50,
    text="🧹 LIMPAR",
    fg_color="#292943",
    hover_color="#414163",
    text_color="white",
    font=("Arial", 15, "bold"),
    corner_radius=12,
    cursor="hand2",
    command=limpar
)
botao_limpar.pack(side="left", padx=8)


texto_progresso = ctk.CTkLabel(
    janela,
    text="DESEMPENHO ACADÊMICO",
    font=("Arial", 14, "bold"),
    text_color="#00E5FF"
)
texto_progresso.pack(pady=(5, 8))


progresso = ctk.CTkProgressBar(
    janela,
    width=450,
    height=18,
    corner_radius=10,
    progress_color="#00E5FF",
    fg_color="#292943"
)
progresso.pack()
progresso.set(0)


resultado = ctk.CTkLabel(
    janela,
    width=500,
    height=135,
    text="Preencha as notas para começar!",
    font=("Arial", 19, "bold"),
    text_color="white",
    fg_color="#24243A",
    corner_radius=18,
    justify="center",
    wraplength=460
)
resultado.pack(pady=22)


rodape = ctk.CTkLabel(
    janela,
    text="NEON SCHOOL  •  TECNOLOGIA E EDUCAÇÃO",
    text_color="#777799",
    font=("Arial", 11)
)
rodape.pack(side="bottom", pady=12)


janela.mainloop()