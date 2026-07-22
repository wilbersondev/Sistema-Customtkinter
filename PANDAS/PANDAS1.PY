import pandas as pd 

dados = {
    "nomes": ["Lucas", "Maria", "João"],
    "Idade": [25, 30, 22],
    "Salario": [3000,5000,2500]
}

df = pd.DataFrame(dados) # DataFrame é como uma planilha Excel dentro do python - tem linhas e colubnasg  
print(df)
print(df.shape) # QUANTAS LINHAS E COLUNAS 
print(df.columns) # NOME DAS COLUNAS 
print(df.dtypes) # TIPO DE CADA COLUNA 
print(df.describe()) # ESTATISTICA DOS DADOS 

filtro = df[df["Salario"] > 2800]
print(filtro)