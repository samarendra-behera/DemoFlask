from apps.users.routers import *
from apps.users import users as ubp

ubp.add_url_rule('/', view_func=UserAPIView.as_view('users'))