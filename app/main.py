from flask import Flask
from asgiref.wsgi import WsgiToAsgi

flask_app = Flask(__name__)


@flask_app.route("/")
def index():
    return (
        "<!doctype html>"
        "<html><head><title>Welcome to Flask</title></head>"
        "<body><h1>Welcome to Flask</h1></body></html>"
    )


app = WsgiToAsgi(flask_app)
