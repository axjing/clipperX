

# https://github.com/imfing/keras-flask-deploy-webapp
from flask import Flask, redirect, url_for, request, render_template, Response, jsonify, redirect
# Declare a flask app
app = Flask(__name__,static_folder="./web/static",template_folder="./web/templates",)

@app.route('/', methods=['GET'])
def index():
    # Main page
    return render_template('index.html')

def web_cutter():

    return

def web_transcriber():
    return

def web_daemoner():
    return
if __name__=="__main__":
    app.run(port=5002,threaded=False)
