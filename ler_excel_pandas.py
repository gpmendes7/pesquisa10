import pandas as pd

tabela = pd.read_excel("SIVEP_20220918_EXCEL_MENOS COLUNAS.xlsx")
#tabela = pd.read_excel("SIVEP_20220918_EXCEL_MENOS COLUNAS_MENOS_LINHAS.xlsx")
print(tabela)
for col in tabela:
    print(col)
