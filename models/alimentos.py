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

    def __init__(self, fruit_id, family, name, genus, order, carbohydrates, protein, fat, calories, sugar):

        self.name = name
        self.fruit_id = fruit_id
        self.family = family
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
            'family': self.family,
            'genus': self.genus,
            'order': self.order,
            'nutritions': {

                'carbohydrates': self.carbohydrates,
                'protein': self.protein,
                'fat': self.fat,
                'calories': self.calories,
                'sugar': self.sugar
            }
            } 
        

    @classmethod
    def find_info(cls, fruit_id):
        #cls é a abreviação da classe, nesse caso, é a mesma coisa que esccrever FrutaModel que é o nome da classe
        #query significa consulta, ele consulta o banco de dados e é uma função do sqlalquemy para consultar informações no banco de dados
        fruta = cls.query.filter_by(fruit_id=fruit_id).first()#select * from frutas where fruit_id = fruit_id
        if fruta:
            return fruta
        else:
            return None

    def save_fruit(self):
        banco.session.add(self)
        banco.session.commit()
        
    
