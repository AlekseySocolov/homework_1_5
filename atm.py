def f_atm():
    import os
    import pickle

    try:
        if os.path.exists('history.data'):
            with open('history.data', 'rb') as f:
                personal_account = pickle.load(f)
    except EOFError:
        personal_account = [0, []]  # переменная персонального счета - сумма на счете и история покупок
        print(personal_account)
        print('История операций отсутствует')

    # функция проверки - является ли строка числом типа float
    def is_digit(string):
        try:
            float(string)
            return True
        except ValueError:
            return False

    # функция пополнения счета
    def f_account_replenishment(account):
        indicator = 1
        print('*' * 40)
        print('ПОПОЛНЕНИЕ СЧЕТА:')
        while indicator > 0:
            indicator = 0
            recharge_amount = input('Введите сумму пополнения счета: ')
            if not is_digit(recharge_amount):
                print('Вводите число!')
                indicator = 1
        account[0] += float(recharge_amount)
        return account

    # функция покупки
    def f_purchase (account):
        indicator = 1
        print('*' * 40)
        print('ПОКУПКА:')
        while indicator > 0:
            indicator = 0
            price = input('Введите стоимость покупки: ')
            if not is_digit(price):
                print('Вводите число!')
                indicator = 1
        if float(price) > account[0]:
            print('На счете недостаточно средств')
        else:
            product = input('Введите наименование покупки: ')
            account[0] -= float(price)
            account[1].append ([product,price])
        return account

    # функция истории покупок
    def f_purchase_history (account):
        print('*' * 40)
        print('ИСТОРИЯ ПОКУПОК:')
        for tandem in account[1]:
            print(f'Товар: {tandem[0]} Цена: {tandem[1]}')

    while True:
        print('*' * 40)
        print(f'На вашем счете - {personal_account[0]} рублей')
        print('=' * 40)
        print('МЕНЮ:')
        print('1. Пополнение счета')
        print('2. Покупка')
        print('3. История покупок')
        print('4. Выход')
        print('*' * 40)
        choice = input('Выберите пункт меню: ')
        if choice == '1':
            personal_account = f_account_replenishment(personal_account)
        elif choice == '2':
            personal_account = f_purchase(personal_account)
        elif choice == '3':
            f_purchase_history(personal_account)
        elif choice == '4':
            print('#' * 40)
            print('ВЫ ВЫШЛИ ИЗ ПРОГРАММЫ!')
            with open('history.data', 'wb') as f:
                # записываем в файл историю операций и баланс счета
                pickle.dump(personal_account, f)
            break
        else:
            print('*' * 40)
            print('Неверный пункт меню')

if __name__ == '_main_':
    print('Проверка фукции')
    f_atm()