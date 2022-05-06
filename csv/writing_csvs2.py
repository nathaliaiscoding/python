import csv

with open('employees.csv', mode='w') as employees:
    fieldnames = ['nome', 'job', 'niver']
    employees_writer = csv.DictWriter(
        employees, fieldnames=fieldnames)

    employees_writer.writeheader()
    employees_writer.writerow(
        {'nome': 'Nathalia Laudano', 'job': 'Engenheira de Dados', 'niver': 'Novembro'})
    employees_writer.writerow(
        {'nome': 'Thalita Nunes', 'job': 'Dev Front End', 'niver': 'Dezembro'})
