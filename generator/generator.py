# устанавливаем пакет для генерации данных + заводим данные которые надо сгенерировать
import random

from data.data import Person, Color
from faker import Faker

faker_ru = Faker('ru_RU')
Faker.seed()

def generated_person(): # заводим данные которые надо сгенерировать
    yield Person(
        full_name=faker_ru.first_name() + " " + faker_ru.last_name() + " " + faker_ru.middle_name(),
        firstname=faker_ru.first_name(),
        lastname=faker_ru.last_name(),
        age=random.randint(10,80),
        salary=random.randint(3000,10000),
        department=faker_ru.job(),
        email=faker_ru.email(),
        current_address= faker_ru.address(),
        permanent_address=faker_ru.address(),
        mobile=faker_ru.msisdn(),
    )

def generated_file():
    # генерируем файл для загрузки
    path = rf'C:\Users\kabac\PycharmProjects\auto_ART\filetest{random.randint(0,999)}.txt'
    file = open(path,'w+')
    file.write(f'файл для автоматизации{random.randint(0,999)}')
    file.close()
    return file.name, path

def generated_subject():
    # генерация subject с использованием массива
    subjects = ["Hindi", "English", "Maths", "Physics", "Chemistry", "Biology",
        "Computer Science", "Commerce", "Accounting", "Economics",
        "Arts", "Social Studies", "History", "Civics"]
    return random.choice(subjects)

def generated_state_selected():
    # генерация state с использованием массива
    state = ["NCR", "Uttar Pradesh", "Haryana", "Rajasthan"]
    return random.choice(state)


def generated_city_selected(state):
    # Определяем словарь с городами
    cities = {
        "NCR": ["Delhi", "Gurgaon", "Noida"],
        "Uttar Pradesh": ["Agra", "Lucknow", "Meerut"],
        "Haryana": ["Karnal", "Panipat"],
        "Rajasthan": ["Jaipur", "Jaisalmer"]
    }
    # Проверяем, существует ли указанный штат в словаре
    if state in cities:
        # Выбираем случайный город из списка городов данного штата
        selected_city = random.choice(cities[state])
        return selected_city
    else:
        return "Штат не найден."



def generated_color():
    # вводим генератор цветов из списка доступных для мультиселекта fill_input_multi /  class AutoCompletePage
    yield Color(
        color_name=["Red", "Blue", "Green", "Yellow", "Purple", "Black", "White", "Voilet", "Indigo", "Magenta", "Aqua"]
    )


