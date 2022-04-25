from flask import Flask, abort, request, flash, url_for, redirect, render_template
from flask_sqlalchemy import SQLAlchemy
#from model import Cliente


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:12486W&a@localhost:5432/db_aluguel'
app.config['SECRET_KEY'] = "random string"

db = SQLAlchemy(app)

@app.route('/')
def index():
    return render_template('menu.html')

#----------------------------------------START CLASS CLIENTE--------------------------------------------------
class Cliente(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    nome = db.Column(db.String())
    endereco = db.Column(db.String())
    data_nascimento = db.Column(db.Date())
    email = db.Column(db.String())  #Usando o tipo email do html
    fone = db.Column(db.String())
    doc_identidade = db.Column(db.String())
    cpf = db.Column(db.Integer())
    fiador = db.Column(db.String())

    def __init__(self, nome, endereco, data_nascimento, email, fone, doc_identidade, cpf, fiador):
        self.nome = nome
        self.endereco = endereco
        self.data_nascimento = data_nascimento
        self.email = email
        self.fone = fone
        self.doc_identidade = doc_identidade
        self.cpf = cpf
        self.fiador = fiador

@app.route('/show_all_clientes')
def show_all_clientes():
   return render_template('show_all_clientes.html', clientes = Cliente.query.all() )

@app.route('/new_cliente', methods = ['GET', 'POST'])
def new_cliente():
    
   if request.method == 'POST':
      if not request.form['nome'] or not request.form['endereco'] or not request.form['data_nascimento'] or not request.form['email'] or not request.form['fone'] or not request.form['doc_identidade'] or not request.form['cpf'] or not request.form['fiador']:
         flash('Por favor, preencha todos os campos!', 'error')
      else:
         cliente = Cliente(request.form['nome'], request.form['endereco'], request.form['data_nascimento'], request.form['email'], request.form['fone'], request.form['doc_identidade'], request.form['cpf'], request.form['fiador'])
         db.session.add(cliente)
         db.session.commit()
         flash('Cliente cadastrado com sucesso')
         return redirect(url_for('show_all_clientes'))
   return render_template('new_cliente.html')

@app.route('/cliente/<id>', methods=['GET', 'POST'])
def update_cliente(id):
    cliente = Cliente.query.get_or_404(id)
    #app.logger.info(request.method)

    if request.method == 'GET':
        return render_template('update_cliente.html', cliente = cliente)

    if request.method == 'POST':
        cliente.nome = request.form["nome"]
        cliente.endereco = request.form["endereco"]
        cliente.data_nascimento = request.form["data_nascimento"]
        cliente.email = request.form["email"]
        cliente.fone = request.form["fone"]
        cliente.doc_identidade = request.form["doc_identidade"]
        cliente.cpf = request.form["cpf"]
        cliente.fiador = request.form["fiador"]
        
        db.session.add(cliente)
        db.session.commit()

        flash('Cliente atualizado com sucesso')
        return redirect(url_for('show_all_clientes'))

@app.route('/cliente_delete/<id>', methods=['POST'])
def cliente_delete(id):
    cliente = Cliente.query.get_or_404(id)
    #app.logger.info(request.method)
    if request.method == 'POST':
        if cliente:
            db.session.delete(cliente)
            db.session.commit()
            flash('Cliente excluído com sucesso')
            return redirect(url_for('show_all_clientes'))
        abort(404)
             
#----------------------------------------START CLASS PROPRIETARIO--------------------------------------------------
class Proprietario(db.Model):
    
    id = db.Column(db.Integer, primary_key = True)
    nome = db.Column(db.String())
    endereco = db.Column(db.String())
    data_nascimento = db.Column(db.Date())
    email = db.Column(db.String())   #Usando o tipo email do html
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


@app.route('/show_all_proprietarios')
def show_all_proprietarios():
   return render_template('show_all_proprietarios.html', proprietarios = Proprietario.query.all() )

@app.route('/new_proprietario', methods = ['GET', 'POST'])
def new_proprietario():
    
   if request.method == 'POST':
      if not request.form['nome'] or not request.form['endereco'] or not request.form['data_nascimento'] or not request.form['email'] or not request.form['fone'] or not request.form['doc_identidade'] or not request.form['cpf'] or not request.form['_id_imovel']:
         flash('Por favor, preencha todos os campos!', 'error')
      else:
         proprietario = Proprietario(request.form['nome'], request.form['endereco'], request.form['data_nascimento'], request.form['email'], request.form['fone'], request.form['doc_identidade'], request.form['cpf'], request.form['_id_imovel'] )
         db.session.add(proprietario)
         db.session.commit()
         flash('Cliente cadastrado com sucesso')
         return redirect(url_for('show_all_proprietarios'))
   return render_template('new_proprietario.html')

@app.route('/proprietario/<id>', methods=['GET', 'POST'])
def update_proprietario(id):
    proprietario = Proprietario.query.get_or_404(id) #app.logger.info(request.method)

    if request.method == 'GET':
        return render_template('update_proprietario.html', proprietario = proprietario)

    if request.method == 'POST':
        proprietario.nome = request.form["nome"]
        proprietario.endereco = request.form["endereco"]
        proprietario.data_nascimento = request.form["data_nascimento"]
        proprietario.email = request.form["email"]
        proprietario.fone = request.form["fone"]
        proprietario.doc_identidade = request.form["doc_identidade"]
        proprietario.cpf = request.form["cpf"]
        proprietario._id_imovel = request.form["_id_imovel"]
        
        db.session.add(proprietario)
        db.session.commit()

        flash('Proprietario atualizado com sucesso')
        return redirect(url_for('show_all_proprietarios'))

@app.route('/proprietario_delete/<id>', methods=['POST'])
def proprietario_delete(id):
    proprietario = Proprietario.query.get_or_404(id)
    #app.logger.info(request.method)
    print(id)
    if request.method == 'GET':
        return render_template('delete_proprietario.html', proprietario = proprietario)
    if request.method == 'POST':
        if proprietario:
            db.session.delete(proprietario)
            db.session.commit()
            flash('Proprietario excluído com sucesso')
            return redirect(url_for('show_all_proprietarios'))
        abort(404)


#----------------------------------------START CLASS IMÓVEL--------------------------------------------------#
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

@app.route('/show_all_imoveis')
def show_all_imoveis():
   return render_template('show_all_imoveis.html', imoveis = Imovel.query.all() )

@app.route('/new_imovel', methods = ['GET', 'POST'])
def new_imovel():
    
   if request.method == 'POST':
      if not request.form['_id_propriet'] or not request.form['_id_contrato'] or not request.form['ender_imovel'] or not request.form['cep'] or not request.form['descric'] or not request.form['area'] or not request.form['qtde_quartos'] or not request.form['num_matricula'] or not request.form['num_insc_munic']:
         flash('Por favor, preencha todos os campos!', 'error')
      else:
         imovel = Imovel(request.form['_id_propriet'], request.form['_id_contrato'], request.form['ender_imovel'], request.form['cep'], request.form['descric'], request.form['area'], request.form['qtde_quartos'], request.form['num_matricula'], request.form['num_insc_munic'])
         db.session.add(imovel)
         db.session.commit()
         flash('Imovel cadastrado com sucesso')
         return redirect(url_for('show_all_imoveis'))
   return render_template('new_imovel.html')

@app.route('/imovel/<id>', methods=['GET', 'POST'])
def update_imovel(id):
    imovel = Imovel.query.get_or_404(id)
    #app.logger.info(request.method)
    if request.method == 'GET':
        return render_template('update_imovel.html', imovel = imovel)

    if request.method == 'POST':
        imovel._id_propriet = request.form["_id_propriet"]
        imovel._id_contrato = request.form["_id_contrato"]
        imovel.ender_imovel = request.form["ender_imovel"]
        imovel.cep = request.form["cep"]
        imovel.descric = request.form["descric"]
        imovel.area = request.form["area"]
        imovel.qtde_quartos = request.form["qtde_quartos"]
        imovel.num_matricula = request.form["num_matricula"]
        imovel.num_insc_munic = request.form["num_insc_munic"]
        
        db.session.add(imovel)
        db.session.commit()

        flash('Imovel atualizado com sucesso')
        return redirect(url_for('show_all_imoveis'))

@app.route('/imovel_delete/<id>', methods=['POST'])
def imovel_delete(id):
    imovel = Imovel.query.get_or_404(id)
    #app.logger.info(request.method)
    if request.method == 'POST':
        if imovel:
            db.session.delete(imovel)
            db.session.commit()
            flash('Imovel excluído com sucesso')
            return redirect(url_for('show_all_imoveis'))
        abort(404)


#----------------------------------------START CLASS CONTRATO--------------------------------------------------#
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
        self._id_propriet = _id_propriet
        self._id_imovel = _id_imovel
        self.data_assinat = data_assinat
        self.valor_aluguel = valor_aluguel
        self.data_ent_imovel = data_ent_imovel
        self.duracao = duracao
        self.termos = termos
        self.num_regist = num_regist

@app.route('/show_all_contratos')
def show_all_contratos():
   return render_template('show_all_contratos.html', contratos = Contrato.query.all() )

@app.route('/new_contrato', methods = ['GET', 'POST'])
def new_contrato():
    
   if request.method == 'POST':
      if not request.form['_id_cliente'] or not request.form['_id_propriet'] or not request.form['_id_imovel'] or not request.form['data_assinat'] or not request.form['valor_aluguel'] or not request.form['data_ent_imovel'] or not request.form['duracao'] or not request.form['termos'] or not request.form['num_regist']:
         flash('Por favor, preencha todos os campos!', 'error')
      else:
         contrato = Contrato(request.form['_id_cliente'], request.form['_id_propriet'], request.form['_id_imovel'], request.form['data_assinat'], request.form['valor_aluguel'], request.form['data_ent_imovel'], request.form['duracao'], request.form['termos'], request.form['num_regist'])
         db.session.add(contrato)
         db.session.commit()
         flash('Contrato cadastrado com sucesso')
         return redirect(url_for('show_all_contratos'))
   return render_template('new_contrato.html')

@app.route('/contrato/<id>', methods=['GET', 'POST'])
def update_contrato(id):
    contrato = Contrato.query.get_or_404(id)
    #app.logger.info(request.method)

    if request.method == 'GET':
        return render_template('update_contrato.html', contrato = contrato)

    if request.method == 'POST':
        contrato._id_cliente = request.form["_id_cliente"]
        contrato._id_propriet = request.form["_id_propriet"]
        contrato._id_imovel = request.form["_id_imovel"]
        contrato.data_assinat = request.form["data_assinat"]
        contrato.valor_aluguel = request.form["valor_aluguel"]
        contrato.data_ent_imovel = request.form["data_ent_imovel"]
        contrato.duracao = request.form["duracao"]
        contrato.termos = request.form["termos"]
        contrato.num_regist = request.form["num_regist"]
        
        db.session.add(contrato)
        db.session.commit()

        flash('Contrato atualizado com sucesso')
        return redirect(url_for('show_all_contratos'))

@app.route('/contrato_delete/<id>', methods=['POST'])
def contrato_delete(id):
    contrato = Contrato.query.get_or_404(id)
    #app.logger.info(request.method)
    if request.method == 'POST':
        if contrato:
            db.session.delete(contrato)
            db.session.commit()
            flash('Contrato excluído com sucesso')
            return redirect(url_for('show_all_contratos'))
        abort(404)

#----------------------------CHAMADA ARQUIVO PRINCIPAL----------------------------------------#
if __name__ == '__main__':
   db.create_all()
   app.run(debug = False)