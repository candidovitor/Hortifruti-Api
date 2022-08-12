from database import banco

class FrutaModel(banco.Model):
    __tablename__ = 'informacao'
    
    fruit_id = banco.Column(banco.Integer, primary_key=True)
    name = banco.Column(banco.String(20))
    family = banco.Column(banco.String(30))
    genus = banco.Column(banco.String(40))
    order = banco.Column(banco.String(40))
    carbohydrates = banco.Column(banco.Integer())
    protein = banco.Column(banco.Integer())
    fat = banco.Column(banco.Integer())
    calories = banco.Column(banco.Integer())
    sugar = banco.Column(banco.Integer())
    
     

    def json(self):
        return {
            
            'name': self.name,
            'fruit_id': self.fruit_id,
            'fammily': self.family,
            'genus': self.genus,
            'order': self.order,
            'carbohydrates': self.carbohydrates,
            'protein': self.protein,
            'fat': self.fat,
            'calories': self.calories,
            'sugar': self.sugar
        }

    
