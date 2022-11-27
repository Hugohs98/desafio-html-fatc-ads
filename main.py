from flask import Flask, render_template, url_for, request, redirect, flash
from flask_mysqldb import MySQL

def create_app():
   from main import routes
   routes.init_app(app)

app = Flask("__Name__")
mysql = MySQL(app)
SECRET_KEY = 'desafio'
app.config["TEMPLATES_AUTO_RELOAD"] = True
app.config.update(
  TEMPLATES_AUTO_RELOAD = True
)

#conexão com o banco de dados
app.config['MYSQL_host']='localhost' # 127.0.0.1
app.config['MYSQL_USER']='root'
app.config['MYSQL_PASSWORD']='1234'
app.config['MYSQL_DB']='contato'

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/quem_somos")
def quem_somos():
    return render_template("quemsomos.html")

@app.route("/contato", methods = ['GET', 'POST'])
def contato():
  if request.method == 'POST':
    email = request.form['email']
    assunto = request.form['assunto']
    descricao = request.form['descricao']

    cur = mysql.connection.cursor()
    cur.execute("INSERT INTO contato(email, assunto, descricao) VALUES (%s, %s, %s)", (email, assunto, descricao))

    mysql.connection.commit()

    cur.close()
    
  return render_template('contato.html')

@app.route('/users')
def users():
    cur = mysql.connection.cursor()

    users = cur.execute("SELECT * FROM contato")

    if users > 0:
      userDetails = cur.fetchall()
      return render_template("users.html", userDetails=userDetails)

if __name__ == '__main__':
  app.run(debug=True)

## python -m venv venv && venv\Scripts\activate && pip install -r requirements.txt && python main.py

