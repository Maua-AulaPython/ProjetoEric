from flask import Flask, request, jsonify
from flask.ext.sqlalchemy import SQLAlchemy
import json

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///mister.db'
from model import *

@app.route('/')
def index():
	return("Hello Sheldon. Para corrigir nosso trabalho sem problemas, nossas rotas são [/mostrar], [/estufa/new], [/medidas/new] !!")
	
@app.route('/mostrar', methods = ['GET'])
def mostraValores():
    medidas = []
	for i in Medida.query.all():
		print (i.id, i.id_estufa, i.localizacao, i.temperatura, i.umidade)
        medidas.append({'id': i.id, 'id_estufa': i.id_estufa, 'localizacao': i.localizacao, 'temperatura':i.temperatura, 'umidade':i.umidademe})

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
    a = Medidas()
    a.estufa_id = p['estufa_id']
    a.temperatura = p['temperatura']
    a.umidade = p['umidade']
    db.session.add(a)
    db.session.commit()
    return jsonify({'status': True})


if __name__ == '__main__':
	app.run(debug=True)
