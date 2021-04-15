from app import db, login_manager
from app import bcrypt
from flask_login import UserMixin


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


PlacesToEndUser = db.Table('PlacesToEndUser',
                           db.Column('user_id', db.Integer, db.ForeignKey(
                               'users.id'), primary_key=True),
                           db.Column('place_id', db.Integer, db.ForeignKey(
                               'places.place_id'), primary_key=True)
                           )


class User(db.Model, UserMixin):
    __tablename__ = 'users'
    id = db.Column(db.Integer(), primary_key=True)
    first_name = db.Column(db.String(length=50))
    last_name = db.Column(db.String(length=50))
    email = db.Column(db.String(length=255), unique=True, nullable=False)
    password_hash = db.Column(db.String(length=60), nullable=False)
    profile_picture_url = db.Column(db.Text)
    data_privacy_accepted = db.Column(db.Boolean(), nullable=False)
    email_marketing_accepted = db.Column(db.Boolean(), nullable=False)
    places = db.relationship('Place', secondary=PlacesToEndUser,
                             lazy='subquery', backref=db.backref('users', lazy=True))

    @property
    def password(self):
        return self.password

    @password.setter
    def password(self, plain_text_password):
        self.password_hash = bcrypt.generate_password_hash(
            plain_text_password).decode('utf-8')

    def check_password_correction(self, attempted_password):
        return bcrypt.check_password_hash(self.password_hash, attempted_password)


class Place(db.Model):
    __tablename__ = 'places'
    place_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(length=255), unique=True, nullable=False)
    street_house_number = db.Column(db.String(length=255), nullable=False)
    postcode = db.Column(db.String(length=5), nullable=False)
    opening_hours = db.relationship(
        'OpeningHours', backref='opening-hours', lazy=True)


class OpeningHours(db.Model):
    opening_id = db.Column(db.Integer(), primary_key=True)
    place_id = db.Column(db.Integer(), db.ForeignKey('places.place_id'))
    week_day = db.Column(db.Integer())
    opens_at = db.Column(db.DateTime())
    closes_at = db.Column(db.DateTime())
