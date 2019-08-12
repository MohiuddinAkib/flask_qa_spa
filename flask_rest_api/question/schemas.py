from .models import Question
from flask_rest_api.extensions import ma


class QuestionSchema(ma.ModelSchema):
    class Meta:
        model = Question
        fields = ('id', 'question', 'answer', 'asked_by_id', 'expert_id', 'links', 'expert', 'asker')

    expert = ma.HyperlinkRelated("user.user_details")
    asker = ma.HyperlinkRelated("user.user_details")
    # Smart hyperlinking
    links = ma.Hyperlinks(
        {"self": ma.URLFor("question.ques", id="<id>"), "collection": ma.URLFor("main.index")}
    )


question_schema = QuestionSchema(strict=True)
questions_schema = QuestionSchema(many=True, strict=True)
