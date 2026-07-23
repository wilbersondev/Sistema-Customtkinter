# Aula 3 - Exportando Dados 

import pandas as pd 

df = pd.read_excel("PANDAS/clientes.xlsx")

filtro = df[df["Faturamento"] > 80000]

filtro_ordenado = filtro.sort_values("Faturamento", ascending=False) # O ascending = "false" -> ordenar em ordem decrecente (maior para menor)
print(filtro_ordenado)
filtro_ordenado.to_csv("resultado.csv", index=False)
filtro_ordenado.to_excel("resultado.xlsx", index=False)
print("Arquivos salvos com sucesso!")

# df.to_csv()	-> Exporta para CSV
# df.to_excel()	-> Exporta para Excel
# index=False	-> Não salva o índice