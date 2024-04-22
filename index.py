from flask import Flask, render_template, request, session, make_response, redirect
import pymysql

app = Flask(__name__)

app.secrete_key = "asdfasdfsadfsdaf1541asdfsf"

db = pymysql.connect(host='localhost', user='root', password='password', database='dankicode')


@app.route('/deletar', methods=['GEt', 'POST'])
def deletar(): 
    cursor = db.cursor()
    sql = 'DELETE FROM clientes WHERE id = %s'
    cursor.execute(sql, (request.args.get('id')))
    db.commit()
    return redirect('/')


@app.route("/", methods=['GET', 'POST'])
def hello_world():
    if request.method == "POST":
        id = request.form.get('id')
        nome = request.form.get('nome')
        email = request.form.get('email')
        cursor = db.cursor()
        sql = 'UPDATE clientes SET nome = %s, email = %s WHERE id = %s'
        cursor.execute(sql, (nome, email, id))
        db.commit()
        return redirect('/')
        # return render_template("index.html", content=resultados)

    
    if request.method == "GET":
        if request.cookies.get("usuario"):
            resp = make_response("Meu website com cookie setado")
        else:
            resp = make_response("Meu website sem cookie!")
            resp.set_cookie("usuario", "Lucas Ramos")

        cursor = db.cursor()
        sql = 'select * from clientes'
        cursor.execute(sql)
        db.commit()
        resultados = cursor.fetchall()
        print(resultados)
        return render_template("index.html", content=resultados)
    else:
        return "O que veio do meu form " + request.form['conteudo']
    
@app.route('/sobre')
def sobre():
    return "<h2> Sobre </h2>"

@app.route('/noticia/<noticia_slug>')
def noticia(noticia_slug):
    return "Noticia: " + noticia_slug

app.run(debug=True)