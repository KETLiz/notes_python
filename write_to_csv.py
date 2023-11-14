import add_model
import csv

def write_to_file():
    note = []
    note = add_model.add_note()
    with open('notes.csv', 'a', newline='', encoding='utf-8') as file:
        writer = csv.writer(file, delimiter=";")
        writer.writerow(note)
