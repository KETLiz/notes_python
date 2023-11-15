import csv
import search_model

# выводит на экран все заметки
def read_from_csv():
    with open('notes.csv', 'r', encoding='utf-8') as file:
        reader = csv.reader(file, delimiter=";")
        for row in reader:
            print(row)
            
# выводит заметку по заданному id
def read_note():
    find_row = search_model.search_note()
    print(find_row)
    
# выводит заметки по выбранной дате
def notes_by_given_date():
    notes = []
    notes = search_model.date_search()
    for note in notes:
        print(note)