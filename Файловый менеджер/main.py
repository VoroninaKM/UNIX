import os
import func

path=os.getcwd()      
print("\n0 - Выход. \n1 - Создать папку.\n2 - Удалить папку.\n3 - Перемещение между папками. \n4 - Создать пустой файл. \n5 - Запись текста в файл. \n6 - Просмотр содержимого файла. \n7 - Удалить файл. \n8 - Копирование файлов из одной папки в другую. \n9 - Перемещение файлов. \n10 - Переименовать файлы.\n")

while True:    
    inputt=int(input())
    if inputt == 0:
        break
    elif inputt == 1:
        func.func1(path)
        continue
    elif inputt == 2:
        func.func2(path)
        continue
    elif inputt == 3:
        path=func.func3(path)
        continue
    elif inputt == 4:
        func.func4(path)
        continue
    elif inputt == 5:
        func.func5(path)
        continue
    elif inputt == 6:
        func.func6(path)
        continue
    elif inputt == 7:
        func.func7(path)
        continue  
    elif inputt == 8:
        func.func8()
        continue
    elif inputt == 9:
        func.func9()
        continue
    elif inputt == 10:
        func.func10()
        continue
    else:
        print("Ошибка!")
        continue