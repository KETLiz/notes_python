def menu():
    print('Выберите режим работы приложения с заметками: ')
    num_command = int(input('1 - добавление\n2 - удаление\n3 - редактирование\n' +
                            '4 - сохранение\n5 - чтение'))
    return num_command

menu()