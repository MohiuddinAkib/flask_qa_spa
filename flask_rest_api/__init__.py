from flask import Flask
from .routes.main import main
from .routes.auth import auth
from .extensions import db, ma, migrate, jwt
from flask_rest_api.user.routes import user
from flask_rest_api.question.routes import question


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
    # init jwt
    jwt.init_app(app)
    # register blueprints
    app.register_blueprint(main, url_prefix='/api')
    app.register_blueprint(auth, url_prefix='/api/auth')
    app.register_blueprint(user, url_prefix='/api/users')
    app.register_blueprint(question, url_prefix='/api/questions')
    # return app
    return app


if __name__ == '__main__':
    create_app()
