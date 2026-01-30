import os
import time
import sys

def typewriter(text): #анимация текста
      for char in text:
            print(char,"\a", end='',flush=True)
            #print('\a')
            time.sleep(0.15)

command = 'cls' if sys.platform == "win32" else "clear" #очистка строки, применять буду так os.system(command)

def bubble_sort_animation(list):
    last = len(list)
    i = 1
    for j in range(last-1):    
        for i in range(last-1-j):
                if list[i] > list[i+1]:
                    change = list[i+1]
                    swap = list[i]
                    list[i] = change
                    list[i+1] = swap
                    typewriter(list)
                    os.system(command)
                    print("\n")
    typewriter(list)

def get_list():
    input("Для того, чтобы добавлять в список числа, вводите их в поле, если нажмете Enter и ничего не введете\nВвод списка будет окончен и начнется сортировка")     
    i = 0
    user_list = []
    user_input = 0
    while user_input != "":
        user_input = input("Задайте лист для сортировки:")
        if user_input !="":
            user_list.insert(int(i), int(user_input))
            i = i + 1
        else:
             break
    return user_list


sort_list = get_list()

bubble_sort_animation(sort_list)
input()
