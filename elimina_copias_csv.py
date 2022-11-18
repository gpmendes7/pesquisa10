import csv

#arquivo1 = 'SIVEP_20220918_csv_MENOS COLUNAS_MENOS_LINHAS_REPETICAO.csv'
#arquivo2 = 'SIVEP_20220918_csv_MENOS COLUNAS_MENOS_LINHAS_REPETICAO_SEM_COPIAS.csv'

arquivo1 = 'SIVEP_20220918_csv_MENOS COLUNAS.csv'
arquivo2 = 'SIVEP_20220918_csv_MENOS COLUNAS_SEM_COPIAS.csv'

registros = {}

with open(arquivo1, 'r') as arq1:
	leitor = csv.reader(arq1, delimiter = ';')	
	contador = 0
	for linha in leitor:
		chave = linha[11] + linha[12] + linha[14]
		print("chave: %s" %(chave))
		if registros.get(chave) != None:
			print("chave duplicada!")
		else: 
			registros[chave] = linha 
		contador += 1
print("número de registros: %d" %(contador-1))
print("número de registros sem cópias: %d" %(len(registros.keys())))

with open(arquivo2, 'w') as arq2:
	escritor = csv.writer(arq2, delimiter = ';', lineterminator = '\n')
	for registro in registros.values():
		escritor.writerow(registro)