from __main__ import app
from flask import render_template

@app.route('/bipolar')

def bipolar():
    return render_template('index.html')