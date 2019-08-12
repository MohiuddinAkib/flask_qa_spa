from flask_rest_api.extensions import db
from werkzeug.security import generate_password_hash
from flask_rest_api.question.models import Question


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))
    password = db.Column(db.String(255))
    expert = db.Column(db.Boolean)
    admin = db.Column(db.Boolean)
    questions_asked = db.relationship(
        Question,
        foreign_keys='Question.asked_by_id',
        backref='asker',
        lazy=True
    )
    answers_requested = db.relationship(
        Question,
        foreign_keys='Question.expert_id',
        backref='expert',
        lazy=True
    )

    @property
    def unhashed_password(self):
        raise AttributeError('Can not show unhashed password')

    @unhashed_password.setter
    def unhashed_password(self, unhashed_password):
        self.password = generate_password_hash(unhashed_password)
