from flask_rest_api.extensions import db


class Question(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    question = db.Column(db.Text)
    answer = db.Column(db.Text)
    asked_by_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    expert_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    def __str__(self):
        return self.question
