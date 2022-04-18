from flask import Flask, abort, request, flash, url_for, redirect, render_template
from flask_sqlalchemy import SQLAlchemy
#from model import Cliente


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:root@localhost:5432/aluguel'
app.config['SECRET_KEY'] = "random string"

db = SQLAlchemy(app)

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


@app.route('/')
def index():
    return render_template('menu.html')

@app.route('/show_all_clientes')
def show_all_clientes():
   return render_template('show_all_clientes.html', clientes = Cliente.query.all() )

@app.route('/new_cliente', methods = ['GET', 'POST'])
def new_cliente():
    
   if request.method == 'POST':
      if not request.form['nome'] or not request.form['endereco'] or not request.form['data_nascimento'] or not request.form['genero'] or not request.form['documento'] or not request.form['iddocumento']:
         flash('Please enter all the fields', 'error')
      else:
         cliente = Cliente(request.form['nome'], request.form['endereco'], request.form['data_nascimento'], request.form['genero'], request.form['documento'], request.form['iddocumento'] )
         
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
        cliente.genero = request.form["genero"]
        cliente.documento = request.form["documento"]
        cliente.iddocumento = request.form["iddocumento"]
        
        db.session.add(cliente)
        db.session.commit()

        flash('Cliente atualizado com sucesso')
        return redirect(url_for('show_all_clientes'))

@app.route('/cliente_delete/<id>', methods=['GET', 'POST'])
def cliente_delete(id):
    cliente = Cliente.query.get_or_404(id)
    #app.logger.info(request.method)
    print(id)
    if request.method == 'GET':
        return render_template('delete_cliente.html', cliente = cliente)
    if request.method == 'POST':
        if cliente:
            db.session.delete(cliente)
            db.session.commit()
            flash('Cliente excluído com sucesso')
            return redirect(url_for('show_all_clientes'))
        abort(404)
             
if __name__ == '__main__':
   db.create_all()
   app.run(debug = True)





