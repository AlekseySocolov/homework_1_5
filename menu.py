import function

function.f_copy_folder_fil()
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
        f_create_folder()
    elif choice == '2':
        personal_account = f_purchase(personal_account)
    elif choice == '3':
        f_purchase_history(personal_account)
    elif choice == '4':
        print('#' * 40)
        print('ВЫ ВЫШЛИ ИЗ ПРОГРАММЫ!')
        break
    else:
        print('*' * 40)
        print('Неверный пункт меню')