import csv

#Caso 1:

def readCsv(path = None):
    if not path:
        path = 'data/reto.csv'
    with open(path, newline='') as file:
        csv_data = csv.reader(file, delimiter=',', quotechar='|')
        return [row for row in csv_data]


if __name__ == '__main__':
    with open('data/reto.csv', newline='') as file:
        reader = csv.reader(file, delimiter=',', quotechar='|')
        for row in reader:
            print(','.join(row))


