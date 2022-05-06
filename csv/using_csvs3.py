import csv

with open('delimitador_aspas.csv') as csv_file:
    csv_reader = csv.DictReader(csv_file, delimiter=',', quotechar='"')
    line_counter = 0

    for row in csv_reader:
        if line_counter == 0:
            print(f'As colunas são {", ".join(row)}.')
            line_counter += 1
        print(
            f'{row["nome"]} trabalha como {row["area"]}, faz aniversário em {row["aniversario"]} e seu endereço é {row["endereco"]}.')
        line_counter += 1

    print(f'Linhas processadas: {line_counter}')
