from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from flask_migrate import Migrate
from flask_jwt_extended import JWTManager
from flask_admin import Admin

db = SQLAlchemy()
ma = Marshmallow()
migrate = Migrate()
jwt = JWTManager()
admin = Admin(name='Flask QA', template_mode='bootstrap3')
