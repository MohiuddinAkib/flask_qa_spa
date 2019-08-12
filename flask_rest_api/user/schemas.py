from .models import User
from flask_rest_api.extensions import ma
from flask_rest_api.question.schemas import QuestionSchema


class UserSchema(ma.ModelSchema):
    class Meta:
        model = User
        exclude = ('password', )
    questions_asked = ma.List(ma.Nested(QuestionSchema, only=['question', 'answer']))
    answers_requested = ma.List(ma.Nested('UserSchema', only=['question']))
    # Smart hyperlinking
    links = ma.Hyperlinks(
        {"self": ma.URLFor("user.user_details", id="<id>"), "collection": ma.URLFor("user.users")}
    )


user_schema = UserSchema(strict=True)
users_schema = UserSchema(many=True, strict=True)
