from flask_rest_api.extensions import db

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))
    password = db.Column(db.String(255))
    expert = db.Column(db.Boolean)
    admin = db.Column(db.Boolean)
    questions_asked = db.relationship(
        'Question',
        foreign_keys='Question.asked_by_id',
        backref='asker',
        lazy=True
    )
    answers_requested = db.relationship(
        'Question',
        foreign_keys='Question.expert_id',
        backref='expert',
        lazy=True
    )
