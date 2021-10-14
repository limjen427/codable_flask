# import admin
from todoFolder import create_app as todoFolder_create_app
admin = todoFolder_create_app()

if __name__ == '__main__':
    admin.run(host='0.0.0.0')