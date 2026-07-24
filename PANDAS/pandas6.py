# Limpeza de Dados 

# df.isnull().sum()      # conta os valores vazios
# df.dropna()            # remove linhas com valores vazios
# df.drop_duplicates()   # remove linhas duplicadas
# df.fillna("Não informado")  # preenche vazios com um valor

import pandas as pd

df = pd.read_excel("PANDAS/novosclientes.xlsx")

print("Valores vazios:")
print(df.isnull().sum())
print("\nSem linhas vazias:")      
print(df.dropna())           
print("\nsem duplicatas:")
print(df.drop_duplicates())
print("\nVazios preenchidos:")  
print(df.fillna("Não informado")) 