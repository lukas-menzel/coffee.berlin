from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import Length, EqualTo, Email, DataRequired
from app.models import User


class RegisterForm(FlaskForm):

    def validate_email(self, email_to_check):
        user = User.query.filter_by(email=email_to_check.data).first()
        if user:
            raise ValidationError(
                'E-Mail-Adress is already in use. Please use a different E-Mail-Adress.')

    first_name = StringField(
        label='First name', validators=[Length(min=2, max=30), DataRequired()])
    last_name = StringField(label='Last name', validators=[Length(min=2, max=30), DataRequired()])
    email = StringField(label='E-Mail-Adress',
                        validators=[Email(), DataRequired()])
    password_hash = PasswordField(label='Password', validators=[
                                  Length(min=8), DataRequired()])
    password_confirm = PasswordField(
        'Confirm Password', validators=[EqualTo('password_hash'), DataRequired()])
    data_privacy_accepted = BooleanField(
        'I accept the data privacy policy.', default=False, validators=[DataRequired()])
    email_marketing_accepted = BooleanField(
        'I want to receive the coffeemap newsletter.', default=False)
    submit = SubmitField(label='Create Account')


class LoginForm(FlaskForm):
    email = StringField(label='E-Mail-Adress',
                        validators=[Email(), DataRequired()])
    password_hash = PasswordField(label='Password', validators=[
                                  Length(min=8), DataRequired()])
    submit = SubmitField(label='Sign in')
