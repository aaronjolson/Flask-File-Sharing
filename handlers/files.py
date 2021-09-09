from flask import jsonify, request
from faker import Faker
fake = Faker()


def make_file():
    Faker.seed(0)
    location = fake.location_on_land()
    latitude = location[0]
    longitude = location[1]
    place_name = location[2]
    country_code = location[3]
    timezone = location[4]
    place_payload = {
        "latitude": latitude,
        "longitude": longitude,
        "placeName": place_name,
        "countryCode": country_code,
        "timezone": timezone
    }
    return place_payload


def file():
    place_payload = make_file()
    return jsonify(place_payload)


def files():
    data = request
    files_list = []
    for x in range(10):
        file = make_file()
        files_list.append(file)
    return jsonify({"places": files_list})
