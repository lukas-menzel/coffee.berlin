from app import app
from flask import render_template, redirect, url_for, flash, get_flashed_messages
from app.models import User, Place, PlacesToEndUser, OpeningHours
from app.forms import RegisterForm, LoginForm
from app import db
from flask_login import login_user, logout_user


@app.route('/')
def index():
    return render_template('index.html', page_title="My great website")


@app.route('/register', methods=['GET', 'POST'])
def register_page():
    form = RegisterForm()
    if form.validate_on_submit():
        user_to_create = User(first_name=form.first_name.data, email=form.email.data, password=form.password_hash.data, data_privacy_accepted=form.data_privacy_accepted.data, email_marketing_accepted=form.email_marketing_accepted.data)
        print(user_to_create.password_hash)
        db.session.add(user_to_create)
        db.session.commit()
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
