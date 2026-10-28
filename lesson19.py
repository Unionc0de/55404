# products = {"Телефон":10000,#Словарь - неупорядоченная коллекция элементов в формате ключ:значение
#             "Книга":500,
#             "Арбуз":500,
#             "Игрушка":400,
#             "Лапти":1000
#             }

# print(products)#Получение всего словаря 
# print(products["Телефон"])#Получение элемента по ключу
# products["Лапти"] = 2000 #Изменение существующего значения
# products["Автомобиль"] = 2000000#Добавление новой пары ключ:значение(если такого ключа в словаре нет)
# del products["Арбуз"] #Удаление элемента по ключу

# if "Пельмени" in products:#Проверка наличия ключа в словаре
#     del products["Пельмени"]

# print(products.keys())#Получение ключей словаря
# print(products.values())#Получение значений словаря

# items = {
#     "Alex":{"phone":"8918234234","city":"Челябинск","age":46},
#     "Alex-pets":["Кошка","Собака","Попугай"]
# }
# print(items["Alex"]["age"])
# print(items["Alex-pets"][1])

product = {"title":"Ноутбук", "price":50000, "discount":10}
product["final_price"] = product["price"] * 0.9
print(product)

a = int(input())
k = int(input())

if a // 2 == k:
    print("+")
else:
    print("-")