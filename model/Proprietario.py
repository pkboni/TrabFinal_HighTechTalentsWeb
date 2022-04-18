from ..app import db

class Proprietario(db.Model):
    
    id = db.Column(db.Integer, primary_key = True)
    idcliente = db.Column(db.Integer())
    dataaluguel = db.Column(db.Date())
    idimovel = db.Column(db.Integer())
    idcorretor = db.Column(db.Integer())
    idcontrato = db.Column(db.Integer())
      
    def __init__(self, nome, endereco, data_nascimento, genero, documento, iddocumento):
        self.nome = nome
        self.endereco = endereco
        self.data_nascimento = data_nascimento
        self.genero = genero
        self.documento = documento
        self.iddocumento = iddocumento
        