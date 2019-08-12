from flask import Blueprint, jsonify

user = Blueprint('user', __name__)


@user.route('/', methods=['GET'])
def users():
    return jsonify("this is users page"), 200

