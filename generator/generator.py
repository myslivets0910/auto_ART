# устанавливаем пакет для генерации данных + заводим данные которые надо сгенерировать
import random

from data.data import Person
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
        department=faker_ru.job() ,
        email=faker_ru.email(),
        current_address= faker_ru.address(),
        permanent_address=faker_ru.address(),
    )

def generated_file():
    # генерируем файл для загрузки
    path = rf'C:\Users\kabac\PycharmProjects\auto_ART\filetest{random.randint(0,999)}.txt'
    file = open(path,'w+')
    file.write(f'файл для автоматизации{random.randint(0,999)}')
    file.close()
    return file.name, path

