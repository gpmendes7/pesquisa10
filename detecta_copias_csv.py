import csv

# nome_arquivo = 'SIVEP_20220918_csv_MENOS COLUNAS.csv'
# nome_arquivo = 'SIVEP_20220918_csv_MENOS COLUNAS_MENOS_LINHAS.csv'
nome_arquivo = 'SIVEP_20220918_csv_MENOS COLUNAS_MENOS_LINHAS_REPETICAO.csv'

with open(nome_arquivo, 'r') as arquivo:
	leitor = csv.reader(arquivo, delimiter = ';')
	registros = {}
	contador = 0
	for linha in leitor:
		chave = linha[11] + linha[12] + linha[14]
		print("chave: %s" %(chave))
		if registros.get(chave) != None:
			print("chave duplicada!")
		else: 
			registros[chave] = linha 
		contador += 1
print("número de registros: %d" %(contador))
print("número de registros sem cópias: %d" %(len(registros.keys())))