from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


def connect_db(app):
    """Connect to database."""

    db.app = app
    db.init_app(app)


class Pet(db.Model):
    """Class for a pet that is potentially up for adoption at the agency."""

    __tablename__ = "pets"

    id = db.Column(db.Integer,
                   primary_key=True,
                   autoincrement=True)
    name = db.Column(db.Text, nullable=False)
    species = db.Column(db.Text, nullable=False)
    photo_url = db.Column(db.Text, nullable=True)
    age = db.Column(db.Integer, nullable=True)
    notes = db.Column(db.Text, nullable=True)
    available = db.Column(db.Boolean, 
                            nullable=False, 
                            default=True)

    def __repr__(self):
        """Displays info for a specific pet."""

        p = self
        return f"<Pet {p.id} {p.name} {p.species} {p.photo_url} {p.age} {p.notes} {p.available}>"
    

