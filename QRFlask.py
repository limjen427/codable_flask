from flask import Flask
from flask_qr import QR


app = Flask(__name__)

qr = QR(app)
img src="{{ qrcode('Do you speak QR?')  }}"

@app.route("/qrFlask")
def QR_flask():
    return "hello world"

{{ 'I am a Qr-Code' | qrFor(https://www.google.com/,dimension=200) }}

