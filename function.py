import os

# добавить папку
def f_create_folder(name_folder):
    return os.mkdir(name_folder) if not os.path.exists(name_folder) else 'Папка с таким именем уже есть!'

# удалить папку/файл
def f_del_folder_file(name_folder_file):
    return os.rmdir(name_folder_file) if os.path.exists(name_folder_file) else 'Папки/файла с таким именем нет!'




# копировать (файл/папку)
def f_copy_folder_file():
    name_copy1_folder_fil = input('Введити имя копируемой папки/файла ')
    if os.path.exists(name_copy1_folder_fil):
        name_copy2_folder_fil = input('Введити имя для новой папки/файла ')
        if not os.path.exists(name_copy2_folder_fil):
            shutil.copyfile(name_copy1_folder_fil, name_copy2_folder_fil)
        else:
            print('Папка/файл с таким именем уже есть!')
    else:
        print('Папки/файла с таким именем нет!')

# просмотр содержимого рабочей директории
def f_view_working_directory ():
    print(os.listdir())

# сохранение информации о содержимом рабочей директории
def f_save_info_directory():
    with open('listdir.txt', 'w') as f:
        f.write(f'files:{f_view_file()}\n')
        f.write(f'dirs:{f_view_folder()}\n')

# посмотреть только папки
def f_view_folder():
    names = os.listdir()
    list_folders = []
    for name in names:
        fullname = os.path.join(name)  # получаем полное имя
        if os.path.isdir(fullname):
            list_folders.append(fullname)
    return list_folders

# посмотреть только файлы
def f_view_file():
    names = os.listdir()
    list_files = []
    for name in names:
        fullname = os.path.join(name)  # получаем полное имя
        if os.path.isfile(fullname):
            list_files.append(fullname)
    return list_files

# просмотр информации об операционной системе
def f_view_os():
    print(os.name)
    print(sys.platform)
    print(platform.uname())

# создатель программы
def f_program_creator():
    return 'Program_creator: Alexey Sokolov from Russia from Orenburg'



