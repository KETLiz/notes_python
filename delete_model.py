import csv
import search_model

def delete_note():
    row_to_delete = search_model.search_note()
    
    f = open('notes.csv', 'r', encoding='utf-8')
    file = csv.reader(f, delimiter=";")
    lists = list(file)
    
    with open('notes.csv', 'w', encoding='utf-8') as file:
        writer = csv.writer(file, delimiter=";")
        for row in lists:
            if row != row_to_delete:
                writer.writerow(row)
            elif row == row_to_delete:
                print('Заметка удалена!')   