# import frontend
from qrFolder import create_app as qrFolder_create_app
frontend = qrFolder_create_app()

if __name__ == '__main__':
    frontend.run(host='0.0.0.0')
