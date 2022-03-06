from flask import Flask, request, render_template, redirect, flash, session
from flask_debugtoolbar import DebugToolbarExtension
from sqlalchemy import false, update
from models import connect_db
from models import Pet, db
from form import AddPetForm, EditPetForm
 

app = Flask(__name__)

app.config['SECRET_KEY'] = "secret"
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///adopt_db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False
debug = DebugToolbarExtension(app)

connect_db(app)

@app.route('/', methods = ['GET'])
def home_page():
    """display homepage with list of pets"""

    pets = Pet.query.order_by(Pet.id.asc()).all()

    return render_template('home.html', pets=pets)

@app.route('/add', methods = ['GET', 'POST'])
def add_pet():
    """render new pet form"""

    form = AddPetForm()

    if form.validate_on_submit():
        name = form.name.data
        species = form.species.data
        photo_url = form.photo_url.data
        age = form.age.data
        notes = form.notes.data
        pet = Pet(name = name, species = species, photo_url = photo_url,
                   age = age, notes = notes)
        
        db.session.rollback()

        db.session.add(pet)
        
        db.session.commit()

        flash(f"Added {name} to Database!")

        return redirect('/')
    
    else:
        
        return render_template('/add_pet_form.html', form=form)

@app.route('/<int:pet_id>', methods=["GET", "POST"])
def show_pet_info(pet_id):
    """ Display pet inoformation. Display pet edit form"""
    
    pet = Pet.query.get_or_404(pet_id)
    
    form =  EditPetForm(obj=pet)

    if form.validate_on_submit():

            pet.photo_url = form.photo_url.data
            pet.notes =  form.notes.data  
            pet.available = form.available.data

            db.session.commit()

            flash(f"{pet.name} updated!")
            
            return redirect('/')
    else:
        return render_template('pet_info.html', pet=pet, form=form)