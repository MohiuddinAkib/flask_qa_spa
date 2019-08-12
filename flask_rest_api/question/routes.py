from .models import Question
from flask_rest_api.extensions import db
from flask import Blueprint, jsonify, request
from .schemas import question_schema, questions_schema
from flask_jwt_extended import jwt_required, get_jwt_identity

question = Blueprint('question', __name__)


@question.route('/ask', methods=['POST'])
@jwt_required
def ask():
    if request.method == 'POST':
        question = request.json.get('question', None)
        expert = request.json.get('expert', None)
        current_user = get_jwt_identity()
        question = Question(question=question, expert_id=expert,
                            asked_by_id=current_user.get('id'))
        db.session.add(question)
        db.session.commit()
        return question_schema.jsonify(
            question
        ), 201


@question.route('/answer/<int:question_id>', methods=['POST'])
@jwt_required
def answer(question_id):
    if request.method == 'POST':
        current_user = get_jwt_identity()
        # get the answer submitted by expert
        answer = request.json.get('answer', None)
        # query the question for expert
        question = Question.query \
            .filter_by(expert_id=current_user.get('id'), id=question_id) \
            .first()
        question.answer = answer
        db.session.commit()
        return question_schema.jsonify(
            question
        ), 200


@question.route('/unanswered', methods=['GET'])
@jwt_required
def unanswered():
    current_user = get_jwt_identity()
    unanswered_questions = Question.query \
        .filter_by(expert_id=current_user.get('id')) \
        .filter(Question.answer == None) \
        .all()
    return questions_schema.jsonify(
        unanswered_questions
    ), 200


@question.route('/<int:id>', methods=['GET'])
def ques(id):
    ques = Question.query.get_or_404(id)
    return questions_schema.jsonify(ques), 200
