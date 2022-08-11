from database import banco

class FrutaModel(banco.Model):
    __tablename__ = 'informacao'
   
    name = banco.Column(banco.String(20))
    fruit_id = banco.Column(banco.Integer, primary_key=True)
    family = banco.Column(banco.String(30))
    genus = banco.Column(banco.String(40))
    order = banco.Column(banco.String(40))
    carbohydrates = banco.Column(banco.Integer())
    protein = banco.Column(banco.Integer())
    fat = banco.Column(banco.Integer())
    calories = banco.Column(banco.Integer())
    sugar = banco.Column(banco.Integer())
    
    def __init__(self, fruit_id, name, genus, order, carbohydrates, protein, fat, calories, sugar):

        self.name = name
        self. fruit_id = fruit_id
        self.genus = genus
        self.order = order
        self.carbohydrates
        self.protein = protein
        self.fat = fat
        self.calories = calories
        self.sugar = sugar

    def json(self):
        return {
            
            'name': self.name,
            'fruit_id': self.fruit_id,
            'genus': self.genus,
            'order': self.order,
        }

    
