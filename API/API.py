import flask
import json

from scrapper import *

app = flask.Flask(__name__)
app.config["DEBUG"] = True


@app.route('/', methods=['GET'])
def home():

    return "<h1>Distant Reading Archive</h1><p>This site is a prototype API for distant reading of science fiction novels.</p>"




@app.route('/cep/correios/', methods=['POST'])
def cep_correios(cep):

    return verifica_cep_correios(cep)






app.run()