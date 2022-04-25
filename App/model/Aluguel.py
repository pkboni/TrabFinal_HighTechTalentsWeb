from flask_sqlalchemy import SQLAlchemy
from ..app import db

db = SQLAlchemy()

class Aluguel(db.Model):
    
    id = db.Column(db.Integer, primary_key = True)
    idcliente = db.Column(db.Integer())
    dataaluguel = db.Column(db.Date())
    idimovel = db.Column(db.Integer())
    idcorretor = db.Column(db.Integer())
    idcontrato = db.Column(db.Integer())
    
    def __init__(self, idcliente, dataaluguel, idimovel, idcorretor, idcontrato):
        self.idcliente = idcliente
        self.dataaluguel = dataaluguel
        self.idimovel = idimovel
        self.idcorretor = idcorretor
        self.idcontrato = idcontrato
        