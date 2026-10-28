# names = ["Александр","Эвелина","Эмелия","Антон","Камиль","MAX","Эмелия","Эмелия"]
# removed = names.pop(0)#Метод, который удаляет элемент списка и его можно сохранить
# print(removed)
# names.sort()#Сортировка списка(по алфавитному порядку или по возрастанию)
# print(names)
# names.reverse()#Разворот списка в обратном порядке
# print(names)

# if "Антон" in names:#Проверка наличия элемента в списке
#     names.remove("Антон")#Перед использованием remove лучше проверить наличие элемента в списке

# print(names.count("Эмелия"))#Считает количество таких элементов в списке
# print(names.index("Эмелия"))#Вовзращает индекс элемента по названию

# numbers = [1,2,3,4,5,6,7,8,9]

# for i in numbers:#можно проходится циклом по списку. i - каждую итерацию будет становится следующим элементом списка
#     print(i*2)

# for index,elem in enumerate(numbers):#enumerate - получение индексов и значений сразу. index - индекс, elem - значение
#     print(f"Идекс :{index} Элемент: {elem*2}")

#Задача 1
dela = []
dela.append("Задача 1")
dela.append("Задача 2")
dela.append("Задача 3")
dela[1] = "Задача выполнена"
print(dela)

#Задача 2
office = ["Alice", "Bob", "Charlie", "Dave"]

if "Eric" not in office:
    office.append("Eric")

office[2] = office[3]
office[3] = "Charlie"
print(office)