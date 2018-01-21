
from flask import Flask
from tigereye.api.misc import MiscView
from tigereye.api.cinema import CinemaView
from tigereye.models import db


def create_app():

    app = Flask(__name__)
    # app.debug = True
    app.config.from_object('tigereye.configs.default.DefaultConfig')
    #注册view到app 中
    MiscView.register(app)
    CinemaView.register(app)
    db.init_app(app)
    return app