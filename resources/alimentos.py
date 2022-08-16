from flask_restful import Resource, reqparse
from models.alimentos import FrutaModel

class Frutas(Resource):
    def get(self):
        return {"frutas": [fruta.json() for fruta in FrutaModel.query.all()]}

class Fruta(Resource):
    argumentos = reqparse.RequestParser()
    argumentos.add_argument('name', type=str, required=True)
    #argumentos.add_argument('fruit_id')
    argumentos.add_argument('family', type=str, required=True)
    argumentos.add_argument('genus', type=str, required=True)
    argumentos.add_argument('order', type=str, required=True)
    argumentos.add_argument('carbohydrates', type=float, required=True)
    argumentos.add_argument('protein', type=float, required=True)
    argumentos.add_argument('fat', type=float, required=True)
    argumentos.add_argument('calories', type=float, required=True)
    argumentos.add_argument('sugar', type=float, required=True)
        
    def get(self, fruit_id):

        fruta = FrutaModel.find_info(fruit_id)
        if fruta:
            return fruta.json()
        else:
            return{"messege": "Fruit not found"}, 404

    def post(self, fruit_id):

        if FrutaModel.find_info(fruit_id):
            return {'message': "Fruit id '{}' already exist".format(fruit_id)}, 400

        dados = Fruta.argumentos.parse_args()
        fruta = FrutaModel(fruit_id, **dados)
        fruta.save_fruit()
        return fruta.json()
        

    def put(self, fruit_id):

            dados = Fruta.argumentos.parse_args()
            nova_fruta = {'fruit_id': fruit_id, **dados}
            dict_fruta = Fruta.find_info(self, fruit_id)

            if dict_fruta:
                
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

                #print(f' post {atualiza_fruta}')
                #print(f'Original {dict_fruta}')

                for key,value in dict_fruta.items():
                    
                    valor_enviado = atualiza_fruta[key]
                    if valor_enviado != value:
                        #print(f'{dict_fruta[key]} mudou de para {valor_enviado}')
                        dict_fruta[key]=valor_enviado
                return dict_fruta, 200

            list_frutas.append(nova_fruta)
            return nova_fruta, 201

            

    def delete(self, fruit_id):

        fruta = FrutaModel.find_info(fruit_id)
        
        if fruta:
            try:
                fruta.delete_fruta()
            except:
                return {'messege': 'An internal error ocurred trying to dalete fruit information.'}, 500
            return {'messesge': 'Fruit deleted'}
        return{'messege':'Fruit deleted'}, 200
            


        
    