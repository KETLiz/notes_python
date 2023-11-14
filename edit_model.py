import csv

# возвращает список с тем id заметки, которую ввёл пользователь
def search_note():
    id = input('Введите id заметки, которую хотите отредактировать: ')
    with open('notes.csv', 'r', encoding='utf-8') as file:
        reader = csv.reader(file, delimiter=";")
        for row in reader:
            if id in row:
                return row
          

# поиск строки тела заметки по выбранному списку
# возвращает тело заметки
def search_body_note(row):
    for i in row:
        return row[3]
   
   
# редактирование заметки
def edit_note(note_body):
    new_note_body = input('Введите новое тело заметки: ')
    with open('notes.csv', 'r', encoding='utf-8') as file:
        reader = csv.reader(file, delimiter=";")
        for row in reader:
            if note_body in row:
                row[3] = new_note_body
                print(row)
    
 
 
search_list_note = search_note()
search_string_note = search_body_note(search_list_note)
#change_body_note = edit_note()
edit_note(search_string_note)