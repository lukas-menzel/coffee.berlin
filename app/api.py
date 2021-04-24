from app import app
from flask import redirect, jsonify, make_response, request
from app.models import User, Place, PlacesToEndUser, OpeningHours
from app import db

@app.route('/place', methods=['GET'])
def get_all_places():

    places = Place.query.all()

    output = []

    for place in places: 
        place_data = {}
        place_date['place_id'] = place.place_id
        place_date['name'] = place.name
        place_date['street_house_number'] = place.street_house_number
        place_data['postcode'] = place.postcode
        output.append(place_data)

    return jsonify({'places' : output})


@app.route('/place/<place_id>', methods=['GET'])
def get_single_place():

    place=Place.query.filter_by().first()

    place_data = {}
    place_date['place_id'] = place.place_id
    place_date['name'] = place.name
    place_date['street_house_number'] = place.street_house_number
    place_data['postcode'] = place.postcode

    return jsonify({'place' : place_data})

@app.route('/place', methods=['POST'])

def create_place(place_id):
    data = request.get_json()

    new_place = Place(name=data['name'], street_house_number=data['street_house_number'], postcode=data['postcode'])
    db.session.add(new_place)
    db.session.commit()

    return jsonify({'message' : 'New place created!'})
