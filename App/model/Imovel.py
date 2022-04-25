from ..app import db

class Imovel(db.Model):
    
    id = db.Column(db.Integer, primary_key = True)
    _id_propriet = db.Column(db.Integer())
    _id_contrato = db.Column(db.Integer())
    ender_imovel = db.Column(db.String())
    cep = db.Column(db.String())
    descric = db.Column(db.String())
    area = db.Column(db.Integer())
    qtde_quartos = db.Column(db.Integer())
    num_matricula = db.Column(db.Integer())
    num_insc_munic = db.Column(db.Integer())
    
    def __init__(self, _id_propriet, _id_contrato, ender_imovel, cep, descric, area, qtde_quartos, num_matricula, num_insc_munic):
        self._id_propriet = _id_propriet
        self._id_contrato = _id_contrato
        self.ender_imovel = ender_imovel
        self.cep = cep
        self.descric = descric
        self.area = area
        self.qtde_quartos = qtde_quartos
        self.num_matricula = num_matricula
        self.num_insc_munic = num_insc_munic
        