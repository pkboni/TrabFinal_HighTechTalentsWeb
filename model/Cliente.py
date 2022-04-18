from ..app import db

class Cliente(db.Model):
    
    id = db.Column(db.Integer, primary_key = True)
    nome = db.Column(db.String())
    endereco = db.Column(db.String())
    data_nascimento = db.Column(db.Date())
    genero = db.Column(db.String())
    documento = db.Column(db.String())
    iddocumento = db.Column(db.Integer())

    def __init__(self, nome, endereco, data_nascimento, genero, documento, iddocumento):
        self.nome = nome
        self.endereco = endereco
        self.data_nascimento = data_nascimento
        self.genero = genero
        self.documento = documento
        self.iddocumento = iddocumento