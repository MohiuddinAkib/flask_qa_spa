from flask_admin import Admin
from flask_migrate import Migrate
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from flask_jwt_extended import JWTManager

db = SQLAlchemy()
ma = Marshmallow()
migrate = Migrate()
jwt = JWTManager()
admin = Admin(name='Flask QA', template_mode='bootstrap3')
cors = CORS()
