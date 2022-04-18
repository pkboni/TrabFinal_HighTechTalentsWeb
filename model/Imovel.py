from ..app import db

class Imovel(db.Model):
    
    id = db.Column(db.Integer, primary_key = True)
    idcliente = db.Column(db.Integer())
    dataaluguel = db.Column(db.Date())
    idimovel = db.Column(db.Integer())
    idcorretor = db.Column(db.Integer())
    idcontrato = db.Column(db.Integer())
    
    def __init__(self, endereco, idproprietario, idtipo, valor_estimado, idstatusalguelvenda):
        self.endereco = endereco
        self.idproprietario = idproprietario
        self.idtipo = idtipo
        self.valor_estimado = valor_estimado
        self.idstatusalguelvenda = idstatusalguelvenda