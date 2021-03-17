import os
import shutil 

def func1(path):
    newdir=str(input("Введите название папки."))
    path+="\\"+newdir
    os.mkdir(path)
    print("Папка создана.")
       
def func2(path):
    delete_dir=str(input("Введите название папки."))
    path+="\\"+delete_dir
    os.rmdir(path)
    print("Папка удалена.")
    
def func3(path):
    go_dir=str(input("Введите название папки."))
    path+="\\"+go_dir
    os.chdir(path)
    return path
    
def func4(path):
    filename=str(input("Введите имя файла."))
    with open(path+"\\"+filename, mode='a'):
        pass
    print("Файл создан.")
        
def func5(path):
    filename=str(input("Введите название файла."))
    text=str(input("Введите текст для записи."))
    with open (path+"\\"+filename, "w") as writer:
        writer.write(text)

def func6(path):
     print ("Введите имя файла.")
     filename=str(input())
     with open (path+"\\"+filename, "r") as f:
         lines=f.readlines()
         for i in lines:
             print(i)

def func7(path):
    filename=str(input("Введите имя файла."))
    os.remove(path+"\\"+filename)
    
def func8():
    filename=str(input("Введите название файла."))
    new_dir=str(input("Введите название папки."))
    shutil.copy(filename, new_dir)

def func9():
    my_file = str(input("Введите путь копируемого файла "))
    my_new_file = str(input("Введите путь назначения нового файла "))
    shutil.move(my_file, my_new_file)

def func10():
    filename=str(input("Введите старое название файла."))
    new_filename=str(input("Введите новое название файла."))
    os.rename(filename, new_filename)

path=os.getcwd()      
print("\n0 - Выход. \n1 - Создать папку.\n2 - Удалить папку.\n3 - Перемещение между папками. \n4 - Создать пустой файл. \n5 - Запись текста в файл. \n6 - Просмотр содержимого файла. \n7 - Удалить файл. \n8 - Копирование файлов из одной папки в другую. \n9 - Перемещение файлов. \n10 - Переименовать файлы.\n")
while True:    
    inputt=int(input())

    if inputt == 0:
        break
    elif inputt == 1:
        func1(path)
        continue
    elif inputt == 2:
        func2(path)
        continue
    elif inputt == 3:
        path=func3(path)
        continue
    elif inputt == 4:
        func4(path)
        continue
    elif inputt == 5:
        func5(path)
        continue
    elif inputt == 6:
        func6(path)
        continue
    elif inputt == 7:
        func7(path)
        continue  
    elif inputt == 8:
        func8()
        continue
    elif inputt == 9:
        func9()
        continue
    elif inputt == 10:
        func10()
        continue
    else:
        print("Ошибка!")
        continue