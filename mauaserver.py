from flask import Flask, request, jsonify
from flask.ext.sqlalchemy import SQLAlchemy
import json

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///Medidas.db'
db = SQLAlchemy(app)
from model import *

@app.route('/')
def index():
	return "Hello Sheldon. Para corrigir nosso trabalho sem problemas, nossas rotas sao [/mostrar], [/estufa/new], [/medidas/new]!!"
	
@app.route('/mostrar', methods = ['GET'])
def mostraValores():
    medidas = []
    for i in Medida.query.all():
        print i.id,i.estufa_id, i.temperatura,i.umidade
        medidas.append({'id': i.id, 'estufa_id': i.estufa_id, 'temperatura':i.temperatura, 'umidade':i.umidade})
    return	json.dumps(medidas)

@app.route('/estufa/new', methods = ['POST'])
def estufa_new():
	if not request.json:
		return jsonify({'status': False})
    p = request.get_json()
	a = Estufa()
	a.localizacao = p['localizacao']
	db.session.add(a)
	db.session.commit()
	return jsonify({'status': True})


@app.route('/medidas/new', methods = ['POST'])
def medida_new():
    if not request.json:
        return jsonify({'status': False})
    p = request.get_json()
    a = Medida()
    a.estufa_id = p['estufa_id']
    a.temperatura = p['temperatura']
    a.umidade = p['umidade']
    db.session.add(a)
    db.session.commit()
    return jsonify({'status': True})


if __name__ == '__main__':
	app.run(debug=True)
