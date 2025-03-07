from database import db

class DataEntry(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    intensity = db.Column(db.Integer)
    likelihood = db.Column(db.Integer)
    relevance = db.Column(db.Integer)
    year = db.Column(db.Integer)
    country = db.Column(db.String(100))
    topic = db.Column(db.String(100))
    region = db.Column(db.String(100))
    city = db.Column(db.String(100))

def create_tables(app):
    with app.app_context():
        db.create_all()
