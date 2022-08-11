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
    },
    {
        'name': 'grape',
        'fruit_id': 'grape',
        'family': 'Vitaceae',
        'genus': 'Vitis',
        'order': 'Vitales',
        'carbohydrates': 17,
        'protein': 0,
        'fat': 0,
        'calories': 67,
        'sugar': 16
    }
]

class informacaos(Resource):
    def get(self):
        return {"informacao": [nome.json() for nome in FrutaModel.query.all()]}