from logging import PlaceHolder
from xmlrpc.client import Boolean
from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, IntegerField, URLField, BooleanField
from wtforms.validators import InputRequired, NumberRange

class AddPetForm(FlaskForm):
    
    name = StringField("Pet Name:", validators=[InputRequired(message="Please add a name")] )
    species = SelectField("Species:", choices = [('cat', 'cat'), ('dog','dog'), ('porcupine', 'porcupine')], validators=[InputRequired()])
    photo_url = URLField("Photo URL:", default = "https://thumbs.dreamstime.com/b/happy-animal-cartoon-illustration-70480578.jpg")
    age = IntegerField("Age:", validators=[NumberRange(min = 0 ,max = 30)])
    notes = StringField("Notes:")

class EditPetForm(FlaskForm):

    photo_url = URLField("Photo URL:" )
    notes = StringField("Notes:")
    available = BooleanField("Available:")