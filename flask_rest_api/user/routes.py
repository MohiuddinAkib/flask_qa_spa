from .models import User
from flask import Blueprint
from flask_rest_api.utils import admin_required
from .schemas import users_schema, user_schema
from flask_rest_api.extensions import db
from flask_jwt_extended import jwt_required

user = Blueprint('user', __name__)


@user.route('/', methods=['GET'])
@jwt_required
def users():
    users = User.query.filter_by(admin=False).all()
    return users_schema.jsonify(users), 200


@user.route('/experts', methods=['GET'])
@jwt_required
def experts():
    experts = User.query.filter_by(expert=True).all()
    return users_schema.jsonify(experts), 200


@user.route('/promote/<int:user_id>', methods=['POST'])
@jwt_required
@admin_required
def promote(user_id):
    user = User.query.get_or_404(user_id)
    user.expert = True
    db.session.commit()
    return user_schema.jsonify(user), 200


@user.route('/demote/<int:user_id>', methods=['POST'])
@jwt_required
@admin_required
def demote(user_id):
    user = User.query.get_or_404(user_id)
    user.expert = False
    db.session.commit()
    return user_schema.jsonify(user), 200


@user.route('/<int:id>', methods=['GET'])
@jwt_required
def user_details(id):
    user = User.query.get_or_404(id)
    return user_schema.jsonify(user), 200
