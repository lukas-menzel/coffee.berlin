from app import app
from flask import render_template, redirect, url_for, flash, get_flashed_messages, jsonify, make_response, request
from app.models import User, Place, PlacesToEndUser, OpeningHours
from app.forms import RegisterForm, LoginForm
from app import db
from flask_login import login_user, logout_user, login_required
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand

@app.route('/')
@login_required
def index():
    return render_template('index.html', page_title="Coffeemap Berlin")

@app.route('/places')
def places():
    return render_template('places.html', page_title="Places")

@app.route('/create-place')
@login_required
def create_place_form():
    return render_template('create-place.html', page_title="Create place")

@app.route('/register', methods=['GET', 'POST'])
def register_page():
    form = RegisterForm()
    if form.validate_on_submit():
        user_to_create = User(first_name=form.first_name.data, last_name=form.last_name.data, email=form.email.data, password=form.password_hash.data, data_privacy_accepted=form.data_privacy_accepted.data, email_marketing_accepted=form.email_marketing_accepted.data)
        db.session.add(user_to_create)
        db.session.commit()

        login_user(user_to_create)
        flash(f'Success! Account created successfully. You are now logged in as: {user_to_create.first_name} ', category='success')
        return redirect(url_for('index'))
    if form.errors != {}:  # If there are no errors from validations
        for err_msg in form.errors.values():
            flash(
                f'There was an error with creating a user: {err_msg}', category='danger')
    return render_template('register.html', form=form)


@app.route('/login', methods=['GET', 'POST'])
def login_page():
    form = LoginForm()
    if form.validate_on_submit():
        attempted_user = User.query.filter_by(email=form.email.data).first()
        if attempted_user and attempted_user.check_password_correction(attempted_password=form.password_hash.data):
            login_user(attempted_user)
            flash(
                'Success! You are logged in as: {attempted_user.first_name} ', category='success')
            return redirect(url_for('index'))
        else:
            flash(
                'E-Mail-adress and password are not match! Please try again.', category='danger')
    return render_template('login.html', form=form)


@app.route('/logout')
def logout_page():
    logout_user()
    flash("You have been logged out!", category='info')
    return redirect(url_for("index"))

@app.route("/profile/<id>")
@login_required
def user(id):
    user = User.query.filter_by(id=id).first_or_404()

    return render_template("profile.html", user=user)

@app.route('/place', methods=['GET'])
def get_all_places():

    places = Place.query.all()

    output = []

    for place in places: 
        place_data = {}
        place_data['id'] = place.id
        place_data['name'] = place.name
        place_data['street_house_number'] = place.street_house_number
        place_data['postcode'] = place.postcode
        place_data['city'] = place.city
        place_data['phone_number'] = place.phone_number
        place_data['email_adress'] = place.email_adress
        place_data['website_url'] = place.website_url
        place_data['facebook_url'] = place.facebook_url
        place_data['instagram_url'] = place.instagram_url
        place_data['wifi_available'] = place.wifi_available
        place_data['toilet_available'] = place.toilet_available
        place_data['power_slots_available'] = place.power_slots_available
        place_data['alcohol_available'] = place.alcohol_available
        place_data['vegan_alternatives_available'] = place.vegan_alternatives_available
        place_data['laptops_allowed'] = place.laptops_allowed
        place_data['open_for_takeaway'] = place.open_for_takeaway
        place_data['open_for_delivery'] = place.open_for_delivery
        place_data['price_espresso'] = place.price_espresso
        place_data['price_filter_coffee'] = place.price_filter_coffee
        place_data['price_cappuccino'] = place.price_cappuccino
        place_data['wifi_network_name'] = place.wifi_network_name
        place_data['wifi_network_password'] = place.wifi_network_password
        place_data['food_options'] = place.food_options
        place_data['picture_urls'] = place.picture_urls



        output.append(place_data)

    return jsonify({'places' : output})


@app.route('/place/<int:id>', methods=['GET'])
def get_single_place(id):

    place = Place.query.filter_by().first()

    place_data = {}
    place_data['id'] = place.id
    place_data['name'] = place.name
    place_data['street_house_number'] = place.street_house_number
    place_data['postcode'] = place.postcode
    place_data['city'] = place.city
    place_data['phone_number'] = place.phone_number
    place_data['email_adress'] = place.email_adress
    place_data['website_url'] = place.website_url
    place_data['facebook_url'] = place.facebook_url
    place_data['instagram_url'] = place.instagram_url
    place_data['wifi_available'] = place.wifi_available
    place_data['toilet_available'] = place.toilet_available
    place_data['power_slots_available'] = place.power_slots_available
    place_data['alcohol_available'] = place.alcohol_available
    place_data['vegan_alternatives_available'] = place.vegan_alternatives_available
    place_data['laptops_allowed'] = place.laptops_allowed
    place_data['open_for_takeaway'] = place.open_for_takeaway
    place_data['open_for_delivery'] = place.open_for_delivery
    place_data['price_espresso'] = place.price_espresso
    place_data['price_filter_coffee'] = place.price_filter_coffee
    place_data['price_cappuccino'] = place.price_cappuccino
    place_data['wifi_network_name'] = place.wifi_network_name
    place_data['wifi_network_password'] = place.wifi_network_password
    place_data['food_options'] = place.food_options
    place_data['picture_urls'] = place.picture_urls

    return jsonify({'place' : place_data})

@app.route('/place', methods=['POST'])

def create_place():
    data = request.get_json()

    new_place = Place(name=data['name'], street_house_number=data['street_house_number'], postcode=data['postcode'], city=data['city'], phone_number=data['phone_number'],email_adress=data['email_adress'], website_url=data['website_url'], facebook_url=data['facebook_url'], instagram_url=data['instagram_url'], wifi_available=data['wifi_available'], toilet_available=data['toilet_available'], power_slots_available=data['power_slots_available'], alcohol_available=data['alcohol_available'], vegan_alternatives_available=data['vegan_alternatives_available'], laptops_allowed=data['laptops_allowed'], open_for_takeaway=data['open_for_takeaway'], open_for_delivery=data['open_for_delivery'], price_espresso=data['price_espresso'], price_filter_coffee=data['price_filter_coffee'], price_cappuccino=data['price_cappuccino'], wifi_network_name=data['wifi_network_name'], wifi_network_password=data['wifi_network_password'])
    # food_options=data['food_options'], picture_urls=data['picture_urls']
    db.session.add(new_place)
    db.session.commit()

    return jsonify({'message' : 'New place created!'})

@app.route('/place/<id>', methods=['PUT'])
def update_place():
    place = Place.query.filter_by(id=id).first()

    if not place:
        return jsonify({'message' : 'No place found.'})
    db.session.commit()

    return jsonify({'message' : 'The place has been updated.'})

@app.route('/place/<id>', methods=['DELETE'])

def delete_place():
    place = Place.query.filter_by(id=id).first()

    if not place:
        return jsonify({'message' : 'No place found.'})
    
    db.session.delete(place)
    db.session.commit()

    return jsonify({'message' : 'The user has been deleted.'})
