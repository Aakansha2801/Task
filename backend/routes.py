from flask import Flask, jsonify, request
from database import init_db, db
from models import DataEntry, create_tables
import pandas as pd

app = Flask(__name__)
init_db(app)
create_tables(app)

@app.route('/load-data', methods=['POST'])
def load_data():
    df = pd.read_json("D:/python AK/Assignment/jsondata.json")
    
    for _, row in df.iterrows():
        entry = DataEntry(
            intensity=row.get('intensity', 0),
            likelihood=row.get('likelihood', 0),
            relevance=row.get('relevance', 0),
            year=int(row.get('start_year', 0)) if row.get('start_year') else None,
            country=row.get('country', ''),
            topic=row.get('topic', ''),
            region=row.get('region', ''),
            city=row.get('city', '')
        )
        db.session.add(entry)
    
    db.session.commit()
    return jsonify({'message': 'Data loaded successfully'})

@app.route('/data', methods=['GET'])
def get_data():
    data = DataEntry.query.all()
    return jsonify([{
        'intensity': d.intensity,
        'likelihood': d.likelihood,
        'relevance': d.relevance,
        'year': d.year,
        'country': d.country,
        'topic': d.topic,
        'region': d.region,
        'city': d.city
    } for d in data])

if __name__ == '__main__':
    app.run(debug=True)
