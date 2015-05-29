from flask import Flask, request, jsonify
from flask.ext.sqlalchemy import SQLAlchemy
from mauaserver import db


class Estufa(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    localizacao = db.Column(db.String(40))

    medidas = db.relationship('Medida')


class Medida(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    id_estufa = db.Column(db.Integer, db.ForeignKey('estufa.id')) 

    umidade = db.Column(db.Float)
    temperatura = db.Column(db.Float)
