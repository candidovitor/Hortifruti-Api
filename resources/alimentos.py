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
            fruta_encontrada = FrutaModel.find_info(fruit_id)
            if fruta_encontrada:
                fruta_encontrada.update_fruta(**dados)
                fruta_encontrada.save_fruit()
                return fruta_encontrada.json(), 200
            fruta = FrutaModel(fruit_id, **dados)
            fruta.save_fruit()
            return fruta.json(), 201
            
    def delete(self, fruit_id):

        fruta = FrutaModel.find_info(fruit_id)
        
        if fruta:
            try:
                fruta.delete_fruta()
            except:
                return {'messege': 'An internal error ocurred trying to dalete fruit information.'}, 500
            return {'messesge': 'Fruit deleted'}
        return{'messege':'Fruit deleted'}, 200
            


        
    