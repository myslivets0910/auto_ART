from dataclasses import dataclass



@dataclass
class Person:
    full_name: str = None
    firstname: str = None
    lastname: str = None
    age: int = None
    salary: int = None
    department: str = None
    email: str = None
    current_address: str = None
    permanent_address: str = None
    mobile: str = None



@dataclass #для class AutoCompletePage
class Color:
    color_name: list = None


@dataclass # для генерации случайной даты
class Date:
    day: list = None
    month: list = None
    year: list = None
    time: list = None