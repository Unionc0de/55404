# import random#Импорт всего модуля (нужно писать название модуля перед вызовом функции)
# from random import randint,choice#Импорт конкретных фунцкий
# from random import *#Импорт всего модуля(не нужно писать название модуля перед вызовом функции)
import time
import datetime

#Рекурсия 
def countdown(num):#Рекурсивная функция
    if num == 0:#Базовый случай(остановка рекурсии)
        print("Отсчет окончен! Старт!")
        return
    print(num)
    countdown(num-1)#Вызов рекурсии(вызов функцией саму себя)

# countdown(5)

def factorial(num):
    if num == 1:#Базовый случай(остановка рекурсии)
        return 1
    return num * factorial(num-1)#Вызов рекурсии

# print(factorial(5))

#Модуль time
# print(time.time())#Количество секунд, которое прошло с 1 января 1970 года
# time.sleep(3)#Задержка на количество секунд в скобках

# start = time.time()#Количество секунд до задержки
# time.sleep(3)
# end = time.time()#Количество секунд после задержки

# print(f"Прошло {end-start} секунд")

#Модуль datetime
# print(datetime.datetime.now())#Получение текущей даты и текущего времени
# print(datetime.date.today())#Получение только текущей даты
# print(datetime.datetime.now().time())#Получение только времени
# print(datetime.datetime.now().year)#получение только года

# time_object = datetime.time(12,34,45)#Создание временного объекта - чч.мм.сс
# print(time_object)

# date_object = datetime.date(2025,11,22)#Создание объекта даты - гггг.мм.дд
# print(date_object)

# datetime_object = datetime.datetime(2025,11,22,12,34,45)
# print(datetime_object)

#timedelta - раздел модуля для работы со временем
# date_now = datetime.datetime.now()#сегодняшняя дата
# print(date_now + datetime.timedelta(days=500))#сегодняшняя дата + 500 дней
# print(date_now - datetime.timedelta(seconds=450000))#сегодняшняя дата - 450000 секунд
# print(date_now + datetime.timedelta(days=500,weeks=400))#сегодняшняя дата - 500 дней и 4 недель

date_str = "2026.11.22"
datetime_str = datetime.datetime(date_str)
print(datetime_str)

print(range(0,6,2))