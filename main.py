#pythonda web uygulaması oluşturmak için küçük bir kullanım

from flask import Flask,render_template #render_template html yi dinamik olarak doldurmak için kullanılır
app = Flask(__name__)
import subprocess  #kullanım yok şu an#Python'un subprocess modülünü içeri aktarır. Bu modül, yeni işlemler başlatmaya, girdi/çıktı/çıktı hatlarına erişmeye ve geri dönüş kodlarını elde etmeye yarar

#burada hello world fonksiyonuna yönlendirme yapılır yani tarayıcıda bu sunucunun adresine  gittiğinde bu fonksiyon çalışır .index.html döner yani
@app.route('/')
def hello_world():
    return render_template("index.html")


# burada suucuyu başlatma işlemi yapılır 
if __name__ == "__main__":
    
    app.run(host='0.0.0.0', port=81)# burada 81 numaralı port üzerinde çalışmasını sağlar 0.0.0.0 olması aynı ağdaki diğer cihazların da erişmesini sağlar
    