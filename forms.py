"""Forms for the pet adoption agency app."""

from flask_wtf import FlaskForm
from wtforms import StringField, FloatField, BooleanField, TextAreaField
from wtforms.validators import InputRequired, Optional, Email

class AddPetForm(FlaskForm):
    """Form for adding pets."""

    name = StringField("Name",
                        validators=[InputRequired()],
                        render_kw={'class': 'form-control'})
    species = StringField("Species",
                            validators=[InputRequired()],
                            render_kw={'class': 'form-control'})
    photo_url = StringField("Photo URL",
                            validators=[Optional()],
                            render_kw={'class': 'form-control'})
    age = FloatField("Age",
                        validators=[InputRequired()],
                        render_kw={'class': 'form-control'})
    notes = TextAreaField("Notes",
                        validators=[Optional()],
                        render_kw={'class': 'form-control', 'rows': 7})
    available = BooleanField("Available",
                                validators=[Optional()])


class EditPetForm(FlaskForm):
    """Form for editing pet info."""

    photo_url = StringField("Photo URL",
                                validators=[Optional()],
                                render_kw={'class': 'form-control'})
    notes = TextAreaField("Notes",
                                validators=[Optional()],
                                render_kw={'class': 'form-control', 'rows': 7})
    available = BooleanField("Available",
                                validators=[Optional()])