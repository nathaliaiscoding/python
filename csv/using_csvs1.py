import csv

with open('employee_birthday.txt') as csv_file:
    csv_reader = csv.DictReader(csv_file, delimiter=',')
    line_counter = 0

    for row in csv_reader:
        if line_counter == 0:
            print(f'As colunas são {", ".join(row)}.')
            line_counter += 1
        print(
            f'{row["nome"]} trabalha como {row["area"]} e faz aniversário em {row["aniversario"]}.')
        line_counter += 1

    print(f'Linhas processadas: {line_counter}')
