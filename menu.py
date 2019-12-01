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
    print('5 - посмотреть только папки')
    print('6 - посмотреть только файлы')
    print('7 - просмотр информации об операционной системе')
    print('8 - создатель программы')
    print('9 - играть в викторину')
    print('10 - мой банковский счет')
    print('11 - выход')
    print('*' * 40)
    choice = input('Выберите пункт меню: ')
    if choice == '1':
        function.f_create_folder()
    elif choice == '2':
        function.f_del_folder_file()
    elif choice == '3':
        function.f_copy_folder_file()
    elif choice == '4':
        function.f_view_working_directory()
    elif choice == '5':
        function.f_view_folder()
    elif choice == '6':
        function.f_view_file()
    elif choice == '7':
        function.f_view_os()
    elif choice == '8':
        print(function.f_program_creator())
    elif choice == '9':
        quiz.f_quiz()
    elif choice == '10':
        atm.f_atm()
    elif choice == '11':
        print('#' * 40)
        print('ВЫ ВЫШЛИ ИЗ ПРОГРАММЫ!')
        break
    else:
        print('*' * 40)
        print('Неверный пункт меню')