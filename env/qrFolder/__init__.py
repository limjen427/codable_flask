from flask import Flask, render_template, request
#from flask_qr import QR
import qrcode
#import os

app = Flask(__name__)

def create_app():
    app_name = 'frontend'
    print('app_name = {}'.format(app_name))

    # create app
    app = Flask(__name__, instance_relative_config=True)

    @app.route("/")
    def hello():
        return 'Hello ' + app_name + '! request.url = ' + request.url
    
    @app.route("/qrCode")
    def qr():
        return render_template("qrCode.html")


    @app.route("/qrCodeNaver")
    def qrN():
        return render_template("qrCodeNaver.html")    


        
    # return app
    return app
