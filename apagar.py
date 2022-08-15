from flask_restful import Resource, reqparse
from models.alimentos import FrutaModel
""" def __init__(self, fruit_id, name, genus, order, carbohydrates, protein, fat, calories, sugar):

        self.name = name
        self.fruit_id = fruit_id
        self.family = family
        self.genus = genus
        self.order = order
        self.carbohydrates
        self.protein = protein
        self.fat = fat
        self.calories = calories
        self.sugar = sugar """

list_frutas = [
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
                return{"information": frutas}

class Fruta(Resource):
        def find_info(self):
                for fruta in list_frutas:
                        print(fruta)

        