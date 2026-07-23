import pandas as pd 
import matplotlib.pyplot as plt 

df = pd.read_excel("PANDAS/clientes.xlsx")

fig, axes = plt.subplots(1, 2, figsize=(12, 5 )) # figsize = (12,5) -> 12 polegadas de largura , 5 de altura - isso define o tamanho da janela do Grafico 

 # Grafico 1  - barras 
df.plot(kind="bar", x="Nome", y="Faturamento", title="Faturamento por Empresa", ax=axes[0])

# Grafico 2 -  pizza 
total_cidade = df.groupby("Cidade")["Faturamento"].sum()
total_cidade.plot(kind="pie", autopct="%1.1f%%", title="Faturamento por Cidade", ax=axes[1])


plt.tight_layout()
plt.show()
