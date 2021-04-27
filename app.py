from flask import Flask, request, render_template, redirect, flash, session
from flask_debugtoolbar import DebugToolbarExtension
from models import db,  connect_db, Pet
from forms import AddPetForm, EditPetForm

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///agency'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True
app.config['SECRET_KEY'] = "ilikemacaroniwitdacheese23"
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False
debug = DebugToolbarExtension(app)

connect_db(app)


@app.route("/")
def home():
    """list the pets' names, photos, and availability."""

    pets = Pet.query.all()
    return render_template("home.html", pets=pets)


@app.route("/add", methods=['GET', 'POST'])
def handle_add_pet_form():
    """Shows a form for adding pets and validates it upon completion."""

    form = AddPetForm()

    if form.validate_on_submit():
        name = form.name.data
        species = form.species.data
        age = form.age.data
        photo_url = form.photo_url.data
        notes = form.notes.data
        available = form.available.data
        p = Pet(name=name, 
                species=species, 
                age=age, 
                photo_url=photo_url, 
                notes=notes, 
                available=available)
        db.session.add(p)
        db.session.commit()

        flash(f"Added {species} named {name} to directory!")
        return redirect("/")

    else:
        flash("Sorry! Something went wrong with your entry. Please try again.")
        return render_template("add_pet.html", form=form)

@app.route("/<int:pet_id>", methods=['GET', 'POST'])
def handle_edit_pet_form(pet_id):
    """shows some information about the pet, a form to edit the pet, and handles pet edits."""

    pet = Pet.query.get_or_404(pet_id)
    form = EditPetForm(obj=pet)

    if form.validate_on_submit():
        pet.photo_url = form.photo_url.data
        pet.notes = form.notes.data
        pet.available = form.available.data
        db.session.commit()
        flash(f"Pet #{pet_id} updated!")
        return redirect("/")

    else:
        flash("Sorry! Something went wrong with your edits. Please try again.")
        return render_template("edit_pet.html", form=form, pet=pet)