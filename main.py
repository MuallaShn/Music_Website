from flask import Flask,render_template, jsonify,request
import json
from recommend import recommend
app = Flask(__name__)
import subprocess

reco_data = ""

@app.route('/')
def main():
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
    try:
        data_toget = recommend.recommendation(reco_data)
    except Exception as e:
        data_toget = ["No Song :("]
    return jsonify(data_toget)




@app.route('/music')
def MusicPage():
    return "Music"

@app.route('/live')
def LivePage():
    return "Live Page"


@app.route('/podcast')
def PodcastPage():
    return "Podcast Page"






if __name__ == "__main__":
    app.run(host='0.0.0.0', port=81)

    
    





