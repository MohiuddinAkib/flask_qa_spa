from flask import Blueprint, jsonify, request, make_response
from flask_rest_api.extensions import db
from flask_rest_api.user.models import User
from flask_rest_api.user.schemas import user_schema
from werkzeug.security import check_password_hash
from flask_jwt_extended import create_access_token

auth = Blueprint('auth', __name__)


@auth.route('/login', methods=['POST'])
def login():
    if request.method == 'POST':
        name = request.json.get('name', None)
        password = request.json.get('password', None)
        user = User.query.filter_by(name=name).first()
        if not user or not check_password_hash(user.password, password):
            return jsonify("Could not login. Please check and try again"), 401
        access_token = create_access_token(identity=user.name)
        response = make_response(jsonify("You have logged in successfully"), 200)
        response.headers['x-auth-token'] = access_token
        response.headers['Access-Control-Expose-Headers'] = 'x-auth-token'
        return response


@auth.route('/register', methods=['POST'])
def register():
    if request.method == 'POST':
        name = request.json.get('name', None)
        unhashed_password = request.json.get('password', None)
        user = User(name=name, unhashed_password=unhashed_password, admin=True, expert=True)
        db.session.add(user)
        db.session.commit()

        return user_schema.jsonify(user), 200
