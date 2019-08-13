import re
from jinja2 import TemplateNotFound
from flask_rest_api.question.models import Question
from flask import Blueprint, jsonify, render_template, abort
from flask_rest_api.question.schemas import questions_schema

main = Blueprint('main', __name__, template_folder='templates',
                 static_folder='static', static_url_path='/')


@main.route('/api/', methods=['GET'])
def index():
    questions = Question.query.filter(Question.answer != None).all()
    return questions_schema.jsonify(questions), 200


@main.route('/', defaults={'u_path': ''})
@main.route('/<path:u_path>')
def client(u_path):
    try:
        return render_template('index.html')
    except TemplateNotFound:
        abort(404)
