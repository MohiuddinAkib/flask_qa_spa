from flask import Blueprint, jsonify

question = Blueprint('question', __name__)


@question.route('/ask', methods=['GET'])
def ask():
    return jsonify(
        'This is ask page'
    ), 200


@question.route('/answer', methods=['GET'])
def answer():
    return jsonify(
        'This is answer page'
    ), 200


@question.route('/unanswered', methods=['GET'])
def unanswered():
    return jsonify(
        'This is unanswered page'
    ), 200
