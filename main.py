import tkinter as tk 
from tkinter import messagebox, simpledialog,filedialog
#Simpledialog -> É uma caixa de dialogo 
#filedialog  -> É uma caixa de dialogo de Arquivos 
 #exibir uma mendagem 
messagebox.showinfo("Sucesso", "Sua automação rodou corretamente ")
# Pega informações do usuario 
nome = simpledialog.askstring("Indentifiação", "Digite seu Nome")

# se o usuario não digita nada, não mostra nada no terminal  
if nome:
    print("Bem vindo", nome)
    # usando o 'else' , caso o usuario não digite nada, o 'else' mostra a  mensagem 
else:
    print("O usuario não informou seu nome ")

    # pegar um arquivo 

arquivo = filedialog.askopenfilename()