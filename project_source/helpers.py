import faker
import string
import random

def get_sign_up_data():
    fake = faker.Faker()
    email = fake.email()
   # password = fake.password
    return email


def get_price():
    fake = faker.Faker()
    price = fake.random_int(100,10000,2)
    return price

def get_text():
    fake = faker.Faker()
    text = fake.credit_card_provider()
    return text

def get_name():
    fake = faker.Faker()
    name = fake.name()
    return name


def get_email():
    result =""
    for num in range(10):
        char = random.choice(string.ascii_lowercase)
        result += char
        return f"{result}@yandex.com"
