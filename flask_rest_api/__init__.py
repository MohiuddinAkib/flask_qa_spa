from flask import Flask
from .extensions import db, ma, migrate


def create_app(config_file='settings.py'):
    # Init app
    app = Flask(__name__)
    # add config file to app config
    app.config.from_pyfile(config_file)
    # Init marshmallow
    ma.init_app(app)
    # Init db
    db.init_app(app)
    # Init migrate
    migrate.init_app(app, db)
    # return app
    return app

if __name__ == '__main__':
    create_app()
