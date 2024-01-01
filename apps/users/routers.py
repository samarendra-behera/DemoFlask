from flask.views import MethodView
from flask import jsonify
from apps.users.models import User


class UserAPIView(MethodView):

    def get(self):
        users:list[User] = User.query.all()
        users_data = [{'id': user.id, 'username': user.username, 'email': user.email} for user in users]
        return jsonify(users_data), 200