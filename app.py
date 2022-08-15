from flask import Flask, render_template
from flask_restful import Api
from resources.alimentos import Frutas, Fruta

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///banco.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
api = Api(app)


@app.before_first_request
def cria_banco():
    banco.create_all()

api.add_resource(Frutas, '/info')
api.add_resource(Fruta, '/info/<int:fruit_id>')
#api.add_resource(Nutritions, '/info/<string:fruit_id>/nutritions')

if __name__ == "__main__":
    from database import banco
    banco.init_app(app)
    app.run(debug=True)