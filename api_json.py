from flask import Flask, make_response, render_template
from db import Carros

app = Flask(__name__)
app.config['json_sort_keys'] = False


@app.route('/')
def index():
    return render_template("index.html")


@app.route('/carros')
def carros():
    return render_template("carros.html")


@app.route('/json/produtos/motos', methods=['GET'])
def get_carros():
    return make_response(Carros)


app.run()
