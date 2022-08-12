from flask_restful import Resource, reqparse
from models.alimentos import FrutaModel

frutas = [
    {
        'fruit_id': 'banana',
        'name': 'banana',       
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
        'fruit_id': 'grape',
        'name': 'grape',
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

class Frutas(Resource):
    def get(self):
        return {"information": frutas}

class Fruta(Resource):
    def get(self, fruit_id):
        for fruta in frutas:
            if fruta['fruit_id'] == fruit_id:
                return fruta
        return {'message': 'Fruit not found'}, 404
        
    def post(self, fruit_id):
        argumentos = reqparse.RequestParser()
        argumentos.add_argument('name')
        argumentos.add_argument('family')
        argumentos.add_argument('genus')
        argumentos.add_argument('order')
        argumentos.add_argument('carbohydrates')
        argumentos.add_argument('protein')
        argumentos.add_argument('fat')
        argumentos.add_argument('calories')
        argumentos.add_argument('sugar')

        dados = argumentos.parse_args()

        print(dados)
        nova_fruta = {
            'fruit_id': fruit_id,
            'name': dados['name'],
            'family': dados['family'],
            'genus': dados['genus'],
            'order': dados['order'],
            'carbohydrates': dados['carbohydrates'],
            'protein': dados['protein'],
            'fat': dados['fat'],
            'calories': dados['calories'],
            'sugar': dados['sugar']
        }

        frutas.append(nova_fruta)
        return nova_fruta, 200


    def put(self, fruit_id):
        pass

  
    
    def delete(self, fruit_id):
        pass

class Nutritions(Resource):
    def get(self, fruit_id, nutrition):
        for fruta in frutas:
                for nutrition in nutritions:
                    if fruta['fruit_id'] == fruit_id and nutrition['nutritions'] == nutritions:
                        return nutritions
    