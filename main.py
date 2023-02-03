#__init__ - мозг класса, отвечает щп созадние оьекта
# 


# class User:
#     """Это класс user"""

#     def __init__(self, name, age):
#         # Иницализируем атрибуты класса
#         self.name =name
#         self.age = age

#     def __str__(self):
#         return f"{self.name} - {self.age}"


# a = User("Jon", 33)
# print(a)

# print(a.__dict__)# - выводит значение в dict

# print(a.__module__)# - показывает что он main

# print(a.__doc__)# - печатает наш коментари класса 

# print(a.__dir__())# - выводит отребуты атрибута

# print(a.__reduce__())



# import random
# import time
# intel = ["core i9", "core i7", "core i5"]
# vc1 = ["GeForce RTX 3070", "GeForce RTX 3080 Ti", "GeForce RTX 3080", "RTX 4000"]
# ma = ["GIGABYTE", "MSI", "ASUS"]
# ram1 = ["16Gb 3200MHz", "32Gb 5200MHz", "32Gb 6000MHz"]
# mem = ["Samsung 970 EVO 1000 GB", " SanDisk 2000 GB", "WD Blue SATA 1000 GB ", "Samsung 860 EVO 500 GB"]
# screen1 = ["15,6 дуймов", "17,3 дуймов", "13 дуймов"]
# name_n = ["Acer", "Lenova", "Asus", "Dell"]
# class Comp:
#     """Что то о ноутбуках"""

#     def __init__(self, core, vc, m, ram, memory, screen, gg, name):
#         self.core = core
#         self.vc = vc
#         self.m = m
#         self.ram = ram 
#         self.memory = memory
#         self.screen = screen
#         self.gg = {}
#         self.name = name

#     def a(self):
#         return f"Процессор - {self.core}: {random.choice(intel)}"

#     def b(self):
#         return f"Видеокарта - {self.vc}: {random.choice(vc1)}"

#     def c(self):
#         return f"Материнка от: {random.choice(ma)}"

#     def d(self):
#         return f"Оперативная память - {self.ram}: {random.choice(ram1)}"

#     def e(self):
#         return f"{self.memory}: {random.choice(mem)}"
    
#     def f(self):
#         return f"Диагональ: {self.screen}"

#     def v(self):
#         return f"Название {self.name}"

#     def __str__(self):
#         return "Получилось что то ..."
    
#     def ggg(self):
#         self.gg.update({
#             f"{self.name}":
#             {"процессор": self.core,
#             "Видеокарта": self.vc,
#             "Материнка:": self.m,
#             "Оперативная память": self.ram,
#             "Память": self.memory,
#             "Диагональ": self.screen}
#         })
#         return self.gg

# comp1 = Comp("Intel", "Nvidia", f"{random.choice(ma)}", "Kingston", "SSD", f"{random.choice(screen1)}", "", f"{random.choice(name_n)}")

# print(comp1.v())
# time.sleep(2)
# print(comp1.a())
# time.sleep(2)
# print(comp1.b())
# time.sleep(2)
# print(comp1.c())
# time.sleep(2)
# print(comp1.d())
# time.sleep(2)
# print(comp1.e())
# time.sleep(2)
# print(comp1.f())
# time.sleep(2)
# print(comp1.ggg())



import requests

class RickMorty:
    """API Rick and Morty"""
    def __init__(self):
        self.url = "https://rickandmortyapi.com/api/"

    def get_info(self, gets):
        response = requests.get(f"{self.url}{gets}")
        data = response.json()
        return data

    def get_episode(self, gets):
        get_id_episode = self.get_info(f"character/{gets}")

        for i in get_id_episode["episode"]:
            response = requests.get(i)
            episode = response.json()
            information_episode = f"""
Эпизод где учавствует персонаж
    Название эпизода: {episode["name"]}
    Дата релиза: {episode["air_date"]}
    Эпизод: {episode["episode"]}
            """
            return information_episode

    
    def get_location(self, gets):
        get_id = self.get_info(f"character/{gets}")
        for i in get_id["location"]:
            name_location = get_id["location"]["name"]
            url_location = get_id["location"]["url"]
            if url_location:
                id_url = url_location.split("/")[-1]
                location = self.get_info(f"location/{id_url}")
                name_dimension = location["dimension"]
                type_location = location["type"]
                information_location = f"""
Локация персонажа
    Название локации: {name_location}
    Тип локации: {type_location}
    Измерение локации: {name_dimension}
                """

                return information_location

            else:
                information_location = f"""
Локация персонажа
    Название локации: {name_location}
    Тип локации: Unknown
    Измерение локации: Unknown 
                """
                return information_location

    
    def get_character_info(self, gets):
        if gets <= 826:
            character = self.get_info(f'character/{gets}')
            information = f"""
            Идентификатор персонажа: {character['id']}
            Имя персонажа: {character['name']}
            Пол персонажа: {character['gender']}
            Жизненное положение: {character['status']}
            Какой расе относится: {character['species']}
            Личность: {character['type']}
            Дата создание: {character['created']}
            
            {self.get_location(gets)}
            {self.get_episode(gets)}
            """

            return information
        return 'Не правильный id персонажа'

    def __str__(self):
        return a.__doc__


b = int(input("Номе персонажа: "))
a = RickMorty()

print(a.get_character_info(b))
print(a)
