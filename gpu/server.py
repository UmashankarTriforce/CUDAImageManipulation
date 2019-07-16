from flask import Flask, request, jsonify, Response
from gaussian_blur import gaussian_blur

app = Flask(__name__)

@app.route('/blur/', methods = ['GET', 'POST'])
def gauss():

    content = request.json
    img = content['matrix']
    out = str(gaussian_blur(img, '800'))

    return out

app.run('0.0.0.0', debug=True)