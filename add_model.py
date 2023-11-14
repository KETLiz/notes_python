import datetime

def add_note():
    id = input('Введите id заметки: ')
    title = input('Введите название заметки: ')
    text = input('Введите текст заметки: ')
    dt_create = datetime.datetime.now()
    
    data = []
    data = [dt_create, id, title, text]
    print('Заметка добавлена!')
    return data

