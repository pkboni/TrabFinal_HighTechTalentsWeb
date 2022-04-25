from ..app import db

class Contrato(db.Model):
    
    id = db.Column(db.Integer, primary_key = True)
    _id_cliente = db.Column(db.Integer())
    _id_propriet = db.Column(db.Integer())
    _id_imovel = db.Column(db.Integer())
    data_assinat = db.Column(db.Date())
    valor_aluguel = db.Column(db.Float())
    data_ent_imovel = db.Column(db.Date())
    duracao = db.Column(db.Integer())
    termos = db.Column(db.String())
    num_regist = db.Column(db.Integer())
    
     
    def __init__(self, _id_cliente, _id_propriet, _id_imovel, data_assinat, valor_aluguel, data_ent_imovel, duracao, termos, num_regist):
        self._id_cliente = _id_cliente
        self._id_propr = _id_propriet
        self._id_imovel = _id_imovel
        self.data_assinat = data_assinat
        self.valor_aluguel = valor_aluguel
        self.data_ent_imovel = data_ent_imovel
        self.duracao = duracao
        self.termos = termos
        self.num_regist = num_regist