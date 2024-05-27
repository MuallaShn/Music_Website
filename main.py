#pythonda web uygulaması oluşturmak için küçük bir kullanım

from flask import Flask,render_template, jsonify,request #render_template html yi dinamik olarak doldurmak için kullanılır
#import json
from recommend import recommend
app = Flask(__name__)
#import subprocess  #kullanım yok şu an#Python'un subprocess modülünü içeri aktarır. Bu modül, yeni işlemler başlatmaya, girdi/çıktı/çıktı hatlarına erişmeye ve geri dönüş kodlarını elde etmeye yarar


reco_data = ""

#burada hello world fonksiyonuna yönlendirme yapılır yani tarayıcıda bu sunucunun adresine  gittiğinde bu fonksiyon çalışır .index2.html döner yani
@app.route('/')
def main():
    return render_template("index2.html")

#Burada  veri alışverişini sağlayacağız url nin post isteği geldiğinde buradaki send_data fonksiyonu çalşacaktır.
@app.route('/send_data', methods=['POST'])
def send_data():
    data_toreceive = request.json

    global reco_data
    reco_data = data_toreceive  #Alınan JSON verisi reco_data global değişkenine atanır.
    return jsonify({'status': 'success', 'data_received': data_toreceive})



@app.route('/get_data', methods=['POST'])
def get_data():
    global reco_data #burada veri depolamak için reco_data tanımladık   
    try:
        data_toget = recommend.recommendation(reco_data) # recommend.recommendation(reco_data) ifadesi çağrılarak, reco_data kullanılarak öneri verileri alınır ve data_toget değişkenine atanır
    except Exception as e:
        data_toget = ["No Song :("]
    return jsonify(data_toget) # değişkeni JSON formatına dönüştürülür ve POST isteği yapan tarafa geri gönderilir.



 #burada htnl içerisinde gerekli sayfalar işlenip kullanıcıya gönderilir live,music ve podcast için ayrı ayrı alınmıştır.
@app.route('/music')
def MusicPage():
    return render_template("music.html")

@app.route('/live')
def LivePage():
    return render_template("live.html")


@app.route('/podcast')
def PodcastPage():
    return render_template("podcast.html")



#burada sunucuya bağlanma işlemini gerçekleştiriyoruz.
if __name__ == "__main__":
    app.run(host='0.0.0.0', port=81)# burada 81 numaralı port üzerinde çalışmasını sağlar 0.0.0.0 olması aynı ağdaki diğer cihazların da erişmesini sağlar

    
    





