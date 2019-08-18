from flask import Flask, request, jsonify, Response
from flops import work
import pycuda.driver as cuda

app = Flask(__name__)

def initialize():

    cuda.init()
    DeviceID = 0
    device = cuda.Device(DeviceID)
    ctx = device.make_context()
    return ctx

def destroy(ctx):
    ctx.pop()

@app.route('/bench', methods = ["GET", "POST"])
def gauss():

    content = request.json
    m = int(content['m'])
    k = int(content['k'])
    n = int(content['n'])
    ctx = initialize()
    out = work(m, k, n)
    output = {
        "Single" : out[0],
        "Double" : out[1]
    }
    destroy(ctx)

    return jsonify(output)

app.run('0.0.0.0',debug=True, port = 80)