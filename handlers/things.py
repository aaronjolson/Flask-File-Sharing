from flask import jsonify, request
from faker import Faker
fake = Faker()


def make_thing(params):
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


def thing():
    place_payload = make_thing()
    return jsonify(place_payload)


def things():
    data = request
    import pdb
    pdb.set_trace()
    things_list = []
    for x in range(10):
        person = make_thing()
        things_list.append(person)
    return jsonify({"places": things_list})
