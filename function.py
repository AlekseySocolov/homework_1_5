# ФУНКЦИИ
import os
import shutil

# добавить папку
def f_create_folder():
    name_folder = input('Введите имя создаваемой папки ')
    if not os.path.exists(name_folder):
        os.mkdir(name_folder)
    else:
        print('Папка с таким именем уже есть!')

# удалить папку/файл
def f_del_folder_fil():
    name_folder_fil = input ('Введите имя удаляемой папки/файла ')
    if os.path.exists(name_folder_fil):
        os.rmdir(name_folder_fil)
    else:
        print('Папки/файла с таким именем нет!')

# копировать (файл/папку)
def f_copy_folder_fil():
    name_copy1_folder_fil = input('Введити имя копируемой папки/файла ')
    if os.path.exists(name_copy1_folder_fil):
        name_copy2_folder_fil = input('Введити имя для новой папки/файла ')
        if not os.path.exists(name_copy2_folder_fil):
            shutil.copyfile(name_copy1_folder_fil,name_copy2_folder_fil)
        else:
            print('Папка/файл с таким именем уже есть!')
    else:
        print('Папки/файла с таким именем нет!')

# просмотр содержимого рабочей директории
def f_view_working_directory ():
    print(os.listdir())

# посмотреть только папки
def f_view_folder():
