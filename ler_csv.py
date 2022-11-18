import csv

# nome_arquivo = 'SIVEP_20220918_csv_MENOS COLUNAS.csv'
nome_arquivo = 'SIVEP_20220918_csv_MENOS COLUNAS_MENOS_LINHAS.csv'

with open(nome_arquivo, 'r') as arquivo:
	leitor = csv.reader(arquivo, delimiter = ';')
	counter = 0
	for row in leitor:
		print("número de colunas: %d" %(len(row)))
		# indice 11 - CPF
		print("cpf: %s" %(row[11]))
		# indice 12 - Nome
		print("nome: %s" %(row[12]))
		# indice 14 - Data de Nascimento
		print("data de nascimento: %s" %(row[14]))
		counter += 1
	print("número de linhas: %d" %(counter))