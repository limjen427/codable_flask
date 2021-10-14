from flask import Flask, render_template
#from flask_qr import QR
import qrcode
#import os

app = Flask(__name__)

@app.route("/")
def index():
    return "This is the index page"

@app.route("/qrCode")
def qr():
    return render_template("qrCode.html")


@app.route("/qrCodeNaver")
def qrN():
    return render_template("qrCodeNaver.html")    

if __name__ == "__main__":
    app.run(debug=True)

