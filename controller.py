import write_to_csv
import view
import edit_model
import delete_model
import read_model

def start():
    view.say_hello()
    while True:
        mode = view.menu()
        if mode == 1:
            write_to_csv.write_to_file()
        elif mode == 2:
            edit_model.edit_note()
        elif mode == 3:
            delete_model.delete_note()
        elif mode == 4:
            read_model.read_from_csv()
        elif mode == 5:
            read_model.read_note()
        elif mode == 6:
            read_model.notes_by_given_date()
        elif mode == 7:
            print('До свидания!')
            break