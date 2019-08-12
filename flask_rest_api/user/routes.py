from flask import Blueprint, jsonify

user = Blueprint('user', __name__)


@user.route('/', methods=['GET'])
def users():
    return jsonify("this is users page"), 200


@user.route('/login', methods=['POST'])
def login():
    return jsonify("this is login page"), 200


@user.route('/register', methods=['POST'])
def register():
    return jsonify("this is register page"), 200
