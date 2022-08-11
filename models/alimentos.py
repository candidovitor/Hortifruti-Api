from database import banco

class FrutaModel(banco.Model):
    __tablename__ = 'informacao'

    fruit_id = banco.Column(banco.Integer, primary_key=True)
    name = banco.Column(banco.String(20))
    family = banco.Column(banco.String(30))
    genus = banco.Column(banco.String(40))
    order = banco.Column(banco.String(40))
    carbohydrates = banco.Column(banco.Float(precision=2))
    protein = banco.Column(banco.Float(precision=2))
    fat = banco.Column(banco.Float(precision=2))
    calories = banco.Column(banco.Float(precision=2))
    sugar = banco.Column(banco.Float(precision=2))
    
    def __init__(self, fruit_id, name, genus, order, carbohydrates, protein, fat, calories, sugar)
    self. fruit_id = fruit_id
    self.name = name
    self.genus = genus
    self.order = order
    self.carbohydrates
    self.protein = protein
    self.fat = fat
    self.calories = calories
    self.sugar = sugar

    def json(self):
        return {
            'fruit_id': self.fruit_id,
            'name': self.name,
            'genus': self.genus,
            'order': self.order,
        }

    
