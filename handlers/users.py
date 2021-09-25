from flask import jsonify
from faker import Faker
fake = Faker()


def make_user():
    name = fake.name()
    address = fake.address()
    phone = fake.phone_number()
    person_payload = {
        "name": name,
        "address": address.replace('\n', ' '),
        "phone": phone
    }
    return person_payload


def user():
    person_payload = make_user()
    return jsonify(person_payload)


def users():
    user_list = []
    for x in range(10):
        user = make_user()
        user_list.append(user)
    return jsonify({"users": user_list})
