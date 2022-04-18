from ..app import db

class Contrato(db.Model):
    
    id = db.Column(db.Integer, primary_key = True)
    idcliente = db.Column(db.Integer())
    dataaluguel = db.Column(db.Date())
    idimovel = db.Column(db.Integer())
    idcorretor = db.Column(db.Integer())
    idcontrato = db.Column(db.Integer())
     
    def __init__(self, idtipocontrato, valor_mes, valor_ano, idtermos, quantidade_meses):
        self.idtipocontrato = idtipocontrato
        self.valor_mes = valor_mes
        self.valor_ano = valor_ano
        self.idtermos = idtermos
        self.quantidade_meses = quantidade_meses
        