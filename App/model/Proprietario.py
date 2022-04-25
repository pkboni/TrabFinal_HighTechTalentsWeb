from ..app import db

class Proprietario(db.Model):
    
    id = db.Column(db.Integer, primary_key = True) 
    nome = db.Column(db.String())
    endereco = db.Column(db.String())
    data_nascimento = db.Column(db.Date())
    email = db.Column(db.String())  #Usando o tipo email do html
    fone = db.Column(db.String())
    doc_identidade = db.Column(db.String())
    cpf = db.Column(db.Integer())
    _id_imovel = db.Column(db.Integer())
      
    def __init__(self, nome, endereco, data_nascimento, email, fone, doc_identidade, cpf, _id_imovel):
        self.nome = nome
        self.endereco = endereco
        self.data_nascimento = data_nascimento
        self.email = email
        self.fone = fone
        self.doc_identidade = doc_identidade
        self.cpf = cpf
        self._id_imovel = _id_imovel
        