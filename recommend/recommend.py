import pandas as pd #pandas kullanarak verileri okumayı sağladık
import nltk  #metni işlemek için bu kütüphaneyi kullandık
from nltk.stem.porter import PorterStemmer #ingilizce kelimelerin köklerini bulmak için kullandık 
stemmer = PorterStemmer()

from sklearn.feature_extraction.text import TfidfVectorizer  # kelimenin ne kadar kullanıldığını ve nerelerde kullanıldığını bulamk için kullanılır 
from sklearn.metrics.pairwise import cosine_similarity #2 vektörü karşılaştırarak benzlerlik bulur ona göre bir çıktı verir ,yukarıdaki metot ile orantılı çalışır


stemmer = PorterStemmer()
df = pd.read_csv("finaldatas.csv") #dosyayı burada okuyoruz ve df ye atıyoruz 



#burada metni kelimelere ayırıp kök bulma işlemi yapıyoruz ,sonra tüm kökü bulunmuş kelimeler birleştirilp daha sonra eğitmek için işimize yarayacak
def tokenization(txt):
    tokens = nltk.word_tokenize(txt)
    stemming = [stemmer.stem(w) for w in tokens]
    return " ".join(stemming)

#print(df)#burada yazdırma işlemi yapıyoruz

tfidvector = TfidfVectorizer(analyzer='word',stop_words='english') #burada metin içerisindeki kelimeleri tespit ediyoruz en çok tekrar edenleri analizliyoruz ,analizin kelimesel olarak aradığını buluyoruz 
matrix = tfidvector.fit_transform(df['text']) #her bir sözcüğün dağacığını öğrenir daha sonra bunları bir vektör haline getirir
#burada kosinus benerliği dediğimiz benzerlik uygulanır. sonuç alınan vektörlerin kosunus benzerliğini alır 1 ve -1 arasında bir sonuç çıkarır 
similarity = cosine_similarity(matrix)


#print(df[df['artist'] == 'Taylor Swift']['song'])# bir filtreleem işleminden geçirilir taylor swift içeren kısımları true alır ve işler daha sonra song kıyaslar ,seçilen sanatçı arafınan söylenen şarkıları çıkarır


def recommendation(song_df):
    idx = df[df['song'] == song_df].index[0] #örnek verilen şarıkının olup olmaıdpını kontrol eder olması durumunda ilk çıkanın index değerini alır

    distances = sorted(list(enumerate(similarity[idx])),reverse=True,key=lambda x:x[1]) #burada benzerlik skorlarını ttespit ediyoruz bir tuple döndürüyoruz buna göre benzzerlik sıralamasıı çıkıyor
    songs = [] #önerilecek şarkıları bir array de tutumak için 
    for m_id in distances[1:21]: #benzer olarak gördüğü ilk 20 eleman alınır

        songs.append(df.iloc[m_id[0]].song) # alınan her şarkı listeye eklenir  iloc belirli bir hücreyi,satırı,sütünu seçmek için genelde kullanılır

        
    return songs  #benzer şarkıları döndürür.






