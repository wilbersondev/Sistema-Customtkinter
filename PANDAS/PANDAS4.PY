import pandas as pd 
import matplotlib.pyplot as plt

df = pd.read_excel("PANDAS/clientes.xlsx")

#Grafico de barras - faturamento por empresa 
df.plot(kind="bar", x="Nome", y="Faturamento", title="Faturamento por Empresa")
plt.tight_layout() #Ajusta automaticamente o espaçamento do gráfico para não cortar os textos nas bordas
plt.show() # ".show" mostra o gráfico 

# ".plot()" -> comando que cria o gráfico a partir do DataFrame
# kind = "bar" -> grafico com barras 
# x = "Nome" -> eixo horizontal
# y = "Faturamento" -> eixo vertical

# Outros tipos de Graficos 

# kind="bar"     -> barras verticais
# kind="barh"    -> barras horizontais
# kind="line"    -> linha
# kind="pie"     -> pizza
# kind="scatter" -> dispersão

total_cidade = df.groupby("Cidade")["Faturamento"].sum()
total_cidade.plot(kind="pie", autopct="%1.1f%%", title="Faturamento por Cidade")
plt.show()