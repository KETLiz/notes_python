import csv

def read_from_csv():
    with open('notes.csv', 'r', encoding='utf-8') as file:
        reader = csv.reader(file)
        for row in reader:
            print(row)
            
read_from_csv()