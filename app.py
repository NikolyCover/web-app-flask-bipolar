from flask import Flask, render_template
from pymysql import connect
from database.ConnectionFactory import ConnectionFactory

app = Flask(__name__)

connection = ConnectionFactory(app)

from controllers import sellers, deolane

if __name__ == "__main__":
    app.run(debug=True)
