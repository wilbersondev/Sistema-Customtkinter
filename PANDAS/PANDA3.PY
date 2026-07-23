import pandas as pd 

df = pd.read_excel("PANDAS/clientes.xlsx")

# ".groupby" -> é um dos comandos mais poderosos do Pandas. Ele agrupa os dados por uma coluna e faz cálculos em cada grupo.
total_fat = df.groupby("Cidade")["Faturamento"].sum() # ".sum()" faz a soma
print("total de faturamento por cidade", total_fat)

media_fat = df.groupby("Cidade")["Faturamento"].mean() # ".mean()"  dá a média 
print("média de faturamento por cidade", media_fat)

quantas_empresas = df.groupby("Cidade")["Faturamento"].count() # ".count()" conta a quantidade 
print("quantas empresas tem em cada cidade", quantas_empresas)