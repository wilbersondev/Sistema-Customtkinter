import tkinter as tk
from tkinter.font import Font

janela = tk.Tk()
janela.title("Sistema de Cadastro de Usuário")
janela.geometry ("900x600")

titulo = tk.Label(text = "Meu APP", font=Font(size=32, weight="bold", family="Arial"))
titulo.pack(pady=(25, 50))

titulo2 = tk.Label(text = "Bem Vindo, Usuário ")
titulo2.pack(pady=(50, 25))

janela.mainloop()