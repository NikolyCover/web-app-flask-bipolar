from __main__ import app, connection
from database.ConnectionFactory import ConnectionFactory
from flask import render_template

@app.route('/')
@app.route("/sellers")

def get_sellers():
    conn = connection.get_connection()
    conn_cursor = conn.cursor()

    conn_cursor.execute('SELECT * FROM seller')
    data = conn_cursor.fetchall()

    for datum in data:
        print(datum)

    return render_template('sellers.html', sellers = data)

@app.route("/sellers/<id>")
def get_by_id(id):

    conn = connection.get_connection()
    c = conn.cursor()
    c.execute(f'SELECT * FROM seller WHERE id = {id} LIMIT 1')
    seller = c.fetchall()
    seller = seller[id]

    return seller

@app.route("/vendedores/cadastrar")
def register():
    return "mostrar formulario de cadastrar"