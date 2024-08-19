import mysql.connector
import os
from flask import Flask, make_response, jsonify, request, render_template

mydb = mysql.connector.connect(
    host = os.getenv('LocalHost'),
    user = os.getenv('User'),
    password = os.getenv('Password'),
    database = os.getenv('DATABASE_URL')
)

app = Flask(__name__)
app.config['json_sort_keys'] = False


@app.route('/')
def index():
    return render_template("index.html")


@app.route('/produtos')
def carros():
    return render_template("carros.html")


@app.route('/carros', methods=['GET'])
def get_carros():

    my_cursor = mydb.cursor()
    my_cursor.execute('SELECT * FROM flask')
    meus_carros = my_cursor.fetchall()

    carros = list()
    for carro in meus_carros:
        carros.append({
            'id': carro[0],
            'marca': carro[1],
            'modelo': carro[2],
            'ano': carro[3]
        })

    return make_response(
        jsonify(
            message='Lista de carros',
            dados=carros
        )
    )


@app.route('/carros/adicionar', methods=['POST'])
def create_carros():
    carro = request.json

    my_cursor = mydb.cursor()
    sql = f"INSERT INTO flask (marca, modelo, ano_lancamento) VALUES ('{carro['marca']}', '{carro['modelo']}', '{carro['ano']}')"
    my_cursor.execute(sql)
    mydb.commit()

    return make_response(
        jsonify(
            message='carro criado com sucesso',
            carro=carro
        )
    )


app.run()
