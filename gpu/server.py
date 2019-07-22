from flask import Flask, request, jsonify, Response
# from gaussian_blur import gaussian_blur
from flops import work
from matplotlib import pyplot as plt
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

@app.route('/bench/')
def gauss():

    # content = request.json
    # img = content['matrix']
    ctx = initialize()
    # img = plt.imread('/gpu/test.jpg')
    out = work()
    output = {
        "Single" : out[0],
        "Double" : out[1]
    }
    destroy(ctx)

    return jsonify(output)

app.run('0.0.0.0',debug=True, port = 80)