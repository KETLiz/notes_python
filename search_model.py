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
    
# ищет заметки по выбранной дате
def date_search():
    input_date = input('Введите дату, по которой совершить выборку, в формате гггг-мм-дд: ')
    f = open('notes.csv', 'r', encoding='utf-8')
    file = csv.reader(f, delimiter=";")
    lists = list(file)
    output_notes = []
    for l in lists:
        date_time = l[0].split(" ")
        date = date_time[0]
        if input_date == date:
            output_notes.append(l)
         
    return output_notes
    file.close()