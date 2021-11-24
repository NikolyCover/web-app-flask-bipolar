from __main__ import app, connection
from database.ConnectionFactory import ConnectionFactory

@app.route('/')
@app.route("/vendedores")

def get_sellers():
    conn = connection.get_connection()
    conn_cursor = conn.cursor()

    conn_cursor.execute('SELECT * FROM seller')
    data = conn_cursor.fetchall()

    for datum in data:
        print(datum)

    return "vendedores"

@app.route("/vendedores/<id>")
def obter_por_id(id):
    return f"obter por id: {id}"

@app.route("/vendedores/cadastrar")
def cadastrar():
    return "mostrar formulario de cadastrar"