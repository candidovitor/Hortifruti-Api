from flask import Flask, render_template
from flask_restful import Api

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///banco.db'
app.config['SQLALCHEMY_TRACK_MODIFICATION'] = False
api = Api(app)

@app.route('/')
def home():
    return render_template('index.html')

@app.before_first_request
def cria_banco():
    banco.create_all()

if __name__ == "__main__":
    from database import banco
    banco.init_app(app)
    app.run(debug=True)