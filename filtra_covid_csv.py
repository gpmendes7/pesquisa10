import csv

arquivo1 = 'SIVEP_20220918_csv_MENOS COLUNAS_SEM_COPIAS.csv'
arquivo2 = 'SIVEP_20220918_csv_MENOS COLUNAS_COM_COVID.csv'
arquivo3 = 'SIVEP_20220918_csv_MENOS COLUNAS_COM_COVID_REDUZIDO.csv'

registros = []

with open(arquivo1, 'r') as arq1:
	leitor = csv.reader(arq1, delimiter = ';')
	contador = 0
	for linha in leitor:
		if (contador == 0) or (linha[78] == '5 - COVID-19'):
			registros.append(linha)
		contador += 1

print("número de registros: %d" %(contador-1))
print("número de registros apenas covid: %d" %(len(registros)))

with open(arquivo2, 'w') as arq2:
	escritor = csv.writer(arq2, delimiter = ';', lineterminator = '\n')
	for registro in registros:
		escritor.writerow(registro)

with open(arquivo3, 'w') as arq3:
	escritor = csv.writer(arq3, delimiter = ';', lineterminator = '\n')
	for registro in registros:
		escritor.writerow((registro[11], registro[12], registro[14], registro[19]))