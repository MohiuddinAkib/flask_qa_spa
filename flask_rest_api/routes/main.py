from flask import Blueprint
from flask_rest_api.question.models import Question
from flask_rest_api.question.schemas import questions_schema

main = Blueprint('main', __name__)


@main.route('/api/', methods=['GET'])
def index():
    questions = Question.query.filter(Question.answer != None).all()
    return questions_schema.jsonify(questions), 200
