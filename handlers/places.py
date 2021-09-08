from flask import jsonify
from faker import Faker
fake = Faker()


def make_place():
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


def place():
    place_payload = make_place()
    return jsonify(place_payload)


def places():
    places_list = []
    for x in range(10):
        person = make_place()
        places_list.append(person)
    return jsonify({"places": places_list})
