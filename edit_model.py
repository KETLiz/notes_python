import csv
import search_model


# редактирование заметки
def edit_note():
    search_list_note = search_model.search_note()
    note_body = search_model.search_body_note(search_list_note)
    new_note_body = input('Введите новое тело заметки: ')
    f = open('notes.csv', 'r', encoding='utf-8')
    file = csv.reader(f, delimiter=";")
    lists = list(file)
    for row in lists:
        if note_body in row:
                row[3] = new_note_body
                print('Заметка изменена!')
    with open('notes.csv', 'w', encoding='utf-8') as file:
        writer = csv.writer(file, delimiter=";")
        writer.writerows(lists)
    