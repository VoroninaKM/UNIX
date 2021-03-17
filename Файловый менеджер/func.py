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