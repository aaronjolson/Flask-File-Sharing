from flask import jsonify
from faker import Faker
fake = Faker()


def make_person():
    name = fake.name()
    address = fake.address()
    phone = fake.phone_number()
    person_payload = {
        "name": name,
        "address": address.replace('\n', ' '),
        "phone": phone
    }
    return person_payload


def person():
    person_payload = make_person()
    return jsonify(person_payload)


def people():
    people_list = []
    for x in range(10):
        person = make_person()
        people_list.append(person)
    return jsonify({"people": people_list})
