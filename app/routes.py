from app import app
import mysql.connector
from flask import request, url_for, redirect, abort, render_template

myDB = mysql.connector.connect(
    host='localhost',
    port=33066,
    user='root',
    password='root',
    database='pruebas_python'
)

cursor = myDB.cursor(dictionary=True)

@app.route('/')
@app.route('/index')
def index():
    return "Hola Mundo - Flask APP"

@app.route('/post/<int:post_id>', methods=['GET', 'POST'])
def lala(post_id):
    if request.method == 'GET':
        return "El id del post es: " + str(post_id)
    else:
        return "Este es otro método y no el GET"

@app.route('/lele', methods=['POST', 'GET'])
def lele():
    # abort(401)
    # return redirect(url_for('lala', post_id=10))
    # print("FORM: ", request.form)
    # print("NAME: ", request.form['name'])
    # print("EMAIL: ", request.form['email'])
    # return "Lele lele"
    cursor.execute("SELECT * FROM test")
    usuarios = cursor.fetchall();
    print(usuarios)
    return render_template('lele.html', usuarios=usuarios)

@app.route('/home', methods=['GET'])
def home():
    return render_template('home.html', titulo="Hola Mundo", footer="Flask - Python")

@app.route('/crear', methods=['GET', 'POST'])
def crear():
    if request.method == 'POST':
        nombre = request.form['nombre']
        email = request.form['email']
        rol = request.form['rol']
        sql = "INSERT INTO test (nombre, email, rol) VALUES (%s,%s,%s)"
        values = (nombre, email, rol)
        cursor.execute(sql, values)
        myDB.commit()

        return redirect(url_for('lele'))

    return render_template('crear.html')

