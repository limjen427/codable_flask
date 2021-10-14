from werkzeug.middleware.dispatcher import DispatcherMiddleware
from werkzeug.serving import run_simple

# import frontend
from qrFolder import create_app as qrFolder_create_app
frontend = qrFolder_create_app()

# import admin
from todoFolder import create_app as todoFolder_create_app
admin = todoFolder_create_app()

# merge
application = DispatcherMiddleware(
    frontend, {
    '/admin': admin
})

if __name__ == '__main__':
    run_simple(
        hostname='localhost',
        port=5000,
        application=application,
        use_reloader=True,
        use_debugger=True,
        use_evalex=True)