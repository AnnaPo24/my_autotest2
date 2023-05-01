
import random

from selenium.webdriver.support.color import Color

from data.data import Person, Date
from faker import Faker

faker_ru = Faker('ru_RU')
faker_en = Faker('En')
Faker.seed()


def get_person():
    yield Person(
        full_name=faker_ru.first_name() + ' ' + faker_ru.last_name(),
        email=faker_ru.email(),
        current_address=faker_ru.address(),
        permanent_address=faker_ru.address(),
        first_name=faker_ru.first_name(),
        last_name=faker_ru.last_name(),
        age=random.randint(1, 100),
        department=faker_ru.job(),
        salary=random.randint(100, 1000000),
        mobile = faker_ru.msisdn()
    )


def generated_file():
    path = rf"C:\Users\aorlova\PycharmProjects\my_autotest2\my_autotest2\test{random.randint(0, 999)}.txt"
    with open(path, 'w+') as f:  # w+ флажок на запись
        f.write(f"""Hello World{random.randint(0, 999)}""")  #записываем в файл строчку
        f.close()
    return f.name, path #возвращаем название и путь


def generated_subject():
    subject = ["Hindi", "English", "Maths", "Physics", "Chemistry", "Biology", "Computer Science",
               "Commerce", "Accounting", "Economics", "Arts", "Social Studies", "History", "Civics"]
    random.shuffle(subject)
    new_list = []
    for i in range(random.randint(1, 4)):
        new_list.append(subject[i])
    return new_list


def generated_city():
    random_list = random.choice(["NCR", "Uttar Pradesh", "Haryana", "Rajasthan"])
    city = {
        "NCR": ["Delhi", "Gurgaon", "Noida"],
        "Uttar Pradesh": ["Agra", "Lucknow", "Merrut"],
        "Haryana": ["Karnal", "Panipat"],
        "Rajasthan": ["Jaipur", "Jaiselmer", ]
    }
    return random_list, city[random_list]


def generator_color():
    yield Color(
        color_name=["Red", "Blue", "Yellow", "Purple", "White", "Violet",
                    "Indigo", "Black", "Magenta", "Aqua", "Green"]
    )

def get_time():
    hours = random.randint(0, 23)
    minutes = random.randint(0, 3) * 15
    time_str = f'{hours:02d}:{minutes:02d}'
    return time_str


def generator_date():
    yield Date(
        year=faker_en.year(),
        month=faker_en.month_name(),
        day=faker_en.day_of_month(),
        time=get_time()
    )



# from faker.providers import internet
#
# fake = Faker()
# fake.add_provider(internet)
# faker_ru = Faker('ru_RU')
#
#
# print(fake.name())
# print(fake.address())
# print(faker_ru.name())
# print(faker_ru.address())
# print(fake.text())
# print(faker_ru.text())
# print(fake.ipv4_private())

