from flask import Flask, render_template

app = Flask(__name__)

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