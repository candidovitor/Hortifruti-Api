from flask_restful import Resource, reqparse
from flask_restful import Resource, reqparse
from models.alimentos import FrutaModel

informacao = [
    {
        'name': 'banana',
        'fruit_id': 'banana',
        'family': 'Musaceae',
        'genus': 'Musa',
        'order': 'Zingiberales',
        'carbohydrates': 23,
        'protein': 1,
        'fat': 0,
        'calories': 89,
        'sugar': 12
    }
]

class informacaos(Resource):
    def get(self):
        return {"informacao": [nome.json() for nome in FrutaModel.query.all()]}