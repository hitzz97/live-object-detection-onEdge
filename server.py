from flask import Flask, render_template, redirect, url_for, request, jsonify,Response
from werkzeug import secure_filename
import os

app = Flask(__name__)
PORT = int(os.getenv('PORT', 8000))


@app.route("/")
def hello():
    return render_template('test.html')

print('Starting Flask!')

app.run(host='127.0.0.1',debug=True,port=PORT)