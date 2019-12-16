import function
import quiz
import atm

while True:
    print('=' * 40)
    print('МЕНЮ:')
    print('1 - создать папку')
    print('2 - удалить (файл/папку)')
    print('3 - копировать (файл/папку)')
    print('4 - просмотр содержимого рабочей директории')
    print('5 - сохранить содержимое рабочей директории в файл')
    print('6 - посмотреть только папки')
    print('7 - посмотреть только файлы')
    print('8 - просмотр информации об операционной системе')
    print('9 - создатель программы')
    print('10 - играть в викторину')
    print('11 - мой банковский счет')
    print('12 - выход')
    print('*' * 40)
    choice = input('Выберите пункт меню: ')
    if choice == '1':
        name_folder = input('Введите имя создаваемой папки ')
        print(function.f_create_folder(name_folder))
    elif choice == '2':
        name_folder_file = input('Введите имя удаляемой папки/файла ')
        print(function.f_del_folder_file(name_folder_file))
    elif choice == '3':
        function.f_copy_folder_file()
    elif choice == '4':
        function.f_view_working_directory()
    elif choice == '5':
        function.f_save_info_directory()
    elif choice == '6':
        print(function.f_view_folder())
    elif choice == '7':
        print(function.f_view_file())
    elif choice == '8':
        function.f_view_os()
    elif choice == '9':
        print(function.f_program_creator())
    elif choice == '10':
        quiz.f_quiz()
    elif choice == '11':
        atm.f_atm()
    elif choice == '12':
        print('#' * 40)
        print('ВЫ ВЫШЛИ ИЗ ПРОГРАММЫ!')
        break
    else:
        print('*' * 40)
        print('Неверный пункт меню')