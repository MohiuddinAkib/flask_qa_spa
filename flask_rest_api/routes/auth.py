from flask_rest_api.extensions import db
from flask_rest_api.user.models import User
from flask_rest_api.user.schemas import user_schema
from flask import Blueprint, jsonify, request, make_response
from flask_jwt_extended import create_access_token, create_refresh_token, jwt_refresh_token_required, get_jwt_identity

auth = Blueprint('auth', __name__)


@auth.route('/login', methods=['POST'])
def login():
    if request.method == 'POST':
        name = request.json.get('name', None)
        password = request.json.get('password', None)
        user = User.query.filter_by(name=name).first()
        if not user or not user.verify_password(password):
            return jsonify("Could not login. Please check and try again"), 401
        # constructing token payload
        token_payload = {'id': user.id, 'name': user.name, 'admin': user.admin}
        access_token = create_access_token(identity=token_payload)
        refresh_token = create_refresh_token(identity=token_payload)
        # Init response
        response = make_response(jsonify("You have logged in successfully"), 200)
        # Setting response header
        response.headers['x-auth-token'] = f"Bearer {access_token}"
        response.headers['x-refresh-token'] = f"Bearer {refresh_token}"
        response.headers['Access-Control-Expose-Headers'] = 'x-auth-token, x-refresh-token'
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


@auth.route('/refresh', methods=['POST'])
@jwt_refresh_token_required
def refresh():
    current_user = get_jwt_identity()
    token_payload = create_access_token(identity=current_user)
    response = make_response(jsonify("Successfully refreshed token"), 201)
    response.headers['x-auth-token'] = f"Bearer {token_payload}"
    response.headers['Access-Control-Expose-Headers'] = 'x-auth-token'
    return response
