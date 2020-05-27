from proje import app
from flask import render_template
import os, platform, requests
from proje.islem import jsonVeri, anahtarlar

uname = platform.uname()

@app.route('/')
def anaSayfa():
    return render_template('grafik.html', baslik="İşte Bunu Seviyorum",
        sistem = uname.system,
        kullanici = os.getlogin(),
        host = uname.node,
        surum = uname.release,
        versiyon = uname.version,
        makine = uname.machine,
        ip = requests.get('http://ip.42.pl/raw').text,
        anahtarlar = anahtarlar,
        veriler = jsonVeri
    )
