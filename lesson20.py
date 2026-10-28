names = {"Ivan":20,"Anna":15,"Maxim":34,"Stepan":25,"Artur":98}

# for name in names:#По умолчанию цикл for проходится по ключам словаря
#     print(name)
#     names[name] += 1#С каждым значением словаря можно совершать какое то дейтсвие по ключу

# for age in names.values():#Возщвращает все значения словаря
#     age += 1#На первоначальный словарь действия не влияют
#     print(age)

# for name in names.keys():#Возвращает все ключи словаря
#     print(name)

# for name,age in names.items():#Возвращает все пары ключ:значение(нужно две переменных-счетчика)
#     age += 1#На первоначальный действия не влияют
#     print(f"Имя-{name}, возраст-{age}")

# print(names)


data = {
    "users":[
        {"name":"Anna","age":20,"role":"admin"},
        {"name":"Artur","age":25,"role":"user"}
    ],
    "emails":[
        {"email":"anna@mail.ru","password":"anna2006"},
        {"email":"artur@mail.ru","password":"artur2001"},
    ]
}

# for user in data["users"]:
#     print(user["age"])

# for password in data["emails"]:
#     print(password["password"])

# shop = {'apple': 50, 'banana': 30, 'cherry': 80}
# sale = {}

# for name,price in shop.items():
#     sale[name] = price*0.8

# print(sale)

grades = {'Ivan': [4,5,4], 
          'Anna': [5,5,5], 
          'Petr': [3,4,4]
          }

for grade in grades:
    for num in grades[grade]:
        print(num)