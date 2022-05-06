import csv

with open('employees.csv', mode='w') as employees:
    employees_writer = csv.writer(
        employees, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)

    employees_writer.writerow(['Nathalia Laudano', 'Engenheira de Dados', 'Novembro'])
    employees_writer.writerow(['Thalita Nunes', 'Dev Front End', 'Dezembro'])
