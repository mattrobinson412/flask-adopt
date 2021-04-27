from app import db
from models import Pet

db.drop_all()
db.create_all()

first_pet = Pet(name="Johnny", 
        species="dog",
        photo_url="https://i.natgeofe.com/n/4f5aaece-3300-41a4-b2a8-ed2708a0a27c/domestic-dog_thumb.jpg",
        age="1",
        notes="Beautiful German Shepherd pup! Looking for a good home."
        )

second_pet = Pet(name="Kathy", 
        species="cat",
        photo_url="https://icatcare.org/app/uploads/2018/06/Layer-1704-1200x630.jpg",
        age="2",
        notes="Charming cat, kind of like Garfield! She can be yours today."
        )

third_pet = Pet(name="Ricky", 
        species="snake",
        photo_url="https://static.dw.com/image/50193312_101.jpg",
        age="4",
        notes="Scary but in a good way! This little cobra is perfect if you have strange children."
        )

db.session.add(first_pet)
db.session.add(second_pet)
db.session.add(third_pet)
db.session.commit()