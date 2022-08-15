from flask_restful import Resource, reqparse
from models.alimentos import FrutaModel

list_frutas = [
    {
        'fruit_id': 1,
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
        'fruit_id': 2,
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
        return {"information": list_frutas}

class Fruta(Resource):
    argumentos = reqparse.RequestParser()
    argumentos.add_argument('fruit_id')
    argumentos.add_argument('name')
    argumentos.add_argument('family')
    argumentos.add_argument('genus')
    argumentos.add_argument('order')
    argumentos.add_argument('carbohydrates')
    argumentos.add_argument('protein')
    argumentos.add_argument('fat')
    argumentos.add_argument('calories')
    argumentos.add_argument('sugar')

    def find_info(self, fruit_id):
        
        for fruta in list_frutas:
            
            if int(fruta['fruit_id']) == int(fruit_id):
                return fruta
        return None
        
    def get(self, fruit_id):

        
        fruta = Fruta.find_info(self, fruit_id)
        print(fruta)
        if fruta:
            return fruta
        else:
            return{"messege": "Fruit not found"}, 404

    def post(self, fruit_id):

        dados = Fruta.argumentos.parse_args()

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

        list_frutas.append(nova_fruta)
        return nova_fruta, 200

    def put(self, fruit_id):

            dados = Fruta.argumentos.parse_args()
            nova_fruta = {'fruit_id': fruit_id, **dados}
            dict_fruta = Fruta.find_info(self, fruit_id)

            if dict_fruta:
                print('atualizar')
                atualiza_fruta = {
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

                print(f' post {atualiza_fruta}')
                print(f'Original {dict_fruta}')

                for key,value in dict_fruta.items():
                    
                    valor_enviado = atualiza_fruta[key]
                    if valor_enviado != value:
                        print(f'{dict_fruta[key]} mudou de para {valor_enviado}')
                        dict_fruta[key]=valor_enviado
                    
                        
                   
                return dict_fruta, 200

            list_frutas.append(nova_fruta)
            return nova_fruta, 201

            

    def delete(self, fruit_id):
        pass 

""" class Nutritions(Resource):
    def get(self, fruit_id, nutrition):
        for fruta in frutas:
                for nutrition in nutritions:
                    if fruta['fruit_id'] == fruit_id and nutrition['nutritions'] == nutritions:
                        return nutritions """
    