import pandas as pd

df = pd.read_excel("PANDAS/clientes.xlsx")


filtro = df[df["Cidade"] == "Teresina"]
print(filtro)

total = filtro["Faturamento"].sum()
print("Faturamento total Teresina: R$", total)

total_geral = df["Faturamento"].sum()
print("Faturamento total geral: R$", total_geral)

# Total de notas emitidas por município
filtro_picos = df[df["Cidade"] == "Picos"]
print(filtro_picos)
total_picos = filtro_picos["Faturamento"].sum()
print("Faturamento total Picos: R$", total_picos)

# df["Coluna"]	        -> Seleciona uma coluna inteira
# df[condição]	        -> Filtra linhas que atendem a condição
# df["Coluna"].sum()	-> Soma todos os valores da coluna
# df["Coluna"].mean()   -> Calcula a média da coluna
# df["Coluna"].max()	-> Pega o maior valor
# df["Coluna"].min()	-> Pega o menor valor

filtro_fat = df[df["Faturamento"] > 100000]
print("Essa são as Empresas que tem o Maior faturamento :", filtro_fat)
            # O "sort_values" É USADO PARA ORDENAR OS DADOS 
ordenado = df.sort_values("Faturamento", ascending=False) # O ascending = "false" -> ordenar em ordem decrecente (maior para menor)
print(ordenado)                                                       # O ascending = "true" -> ordenar em ordem crecente do (menor para o maior)

# pd.read_excel() ->  Lê planilha Excel
# df["Coluna"]	  ->  Seleciona coluna
# df[condição]	  ->  Filtra linhas
# .sum()          ->  Soma valores
# .sort_values()  ->  Ordena dados