from flask import Flask,render_template, jsonify,request
import json
from recommend import recommend
app = Flask(__name__)
import subprocess

reco_data = ""

@app.route('/')
def hello_world():
    return render_template("index.html")

@app.route('/send_data', methods=['POST'])
def send_data():
    data_toreceive = request.json

    global reco_data
    reco_data = data_toreceive
    return jsonify({'status': 'success', 'data_received': data_toreceive})



@app.route('/get_data', methods=['POST'])
def get_data():
    global reco_data
    data_toget = recommend.recommendation(reco_data)
    return jsonify(data_toget)



if __name__ == "__main__":
    app.run(host='0.0.0.0', port=81)

    
    





