import flask
import json
from flask import request

from scrapper import *
from flask import Flask
from flask_cors import CORS

from flask_cors import CORS, cross_origin
import logging


app = Flask(__name__)
CORS(app)
cors = CORS(app, resources={r"/*": {"origins": "*"}})



app = flask.Flask(__name__)
app.config["DEBUG"] = True

app.config['CORS_HEADERS'] = 'Content-Type'











@app.route('/', methods=['GET'])

def home():

    return "<h1>Consulta CEP</h1><p>Consulte a documentação para as rotas!</p>"


@app.route('/cep/logs/', methods=['GET'])
@cross_origin()
def logs():
    return busca_log()




@app.route('/cep/correios/', methods=['POST'])
@cross_origin()
def cep_correios():
    cep = request.json['cep']
    print(cep)
    return verifica_cep_correios(cep)



@app.route('/cep/local/', methods=['POST'])
@cross_origin() 
def cep_local():
    cep = request.json['cep']
    return verifica_cep_local(cep)





app.run()