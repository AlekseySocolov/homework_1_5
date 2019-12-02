from function import *
import os
# тестируем функцию выводящую данные о cоздателе
def test_f_program_creator():
    assert f_program_creator() == 'Program_creator: Alexey Sokolov from Russia from Orenburg'

# тестируем создание папки
def test_f_create_folder():
    f_create_folder('name_folder')
    assert f_create_folder('name_folder') == 'Папка с таким именем уже есть!'
    os.rmdir('name_folder')
    assert f_create_folder('name_folder') == None

# тестируем удаление файла
def test_f_del_folder_file():
    assert f_del_folder_file('name_folder_file.py') == 'Папки/файла с таким именем нет!'
    os.mkdir('name_folder_file.py')
    assert f_del_folder_file('name_folder_file.py') == None
