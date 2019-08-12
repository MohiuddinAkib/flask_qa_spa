from .models import User
from flask_rest_api.extensions import ma


class UserSchema(ma.ModelSchema):
    class Meta:
        model = User
        fields = ('id', 'name', 'expert', 'admin', 'questions_asked', 'answers_requested')

    # questions_asked = ma.HyperlinkRelated('questions_asked')
    # answers_requested = ma.HyperlinkRelated('answers_requested')
    # Smart hyperlinking
    _links = ma.Hyperlinks(
        {"self": ma.URLFor("user_detail", id="<id>"), "collection": ma.URLFor("users")}
    )


user_schema = UserSchema(strict=True)
users_schema = UserSchema(many=True, strict=True)
