from .models import Question
from flask_rest_api.extensions import ma
from flask_rest_api.user.schemas import UserSchema


class QuestionSchema(ma.ModelSchema):
    class Meta:
        model = Question
        fields = ('id', 'question', 'answer', 'asked_by_id', 'expert_id')

    # expert = ma.Nested(UserSchema)
    # asked_by = ma.Nested(UserSchema)
    # Smart hyperlinking
    _links = ma.Hyperlinks(
        {"self": ma.URLFor("question_detail", id="<id>"), "collection": ma.URLFor("questions")}
    )


question_schema = QuestionSchema(strict=True)
questions_schema = QuestionSchema(many=True, strict=True)
