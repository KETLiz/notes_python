import csv

# возвращает список с тем id заметки, которую ввёл пользователь
def search_note():
    id = input('Введите id заметки: ')
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