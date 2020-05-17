from flask_restful import Api

from app.resources.user import UserLogin, UserRegistration
from app.resources.token import TokenRefresh


def load(api: Api) -> Api:

    api.add_resource(TokenRefresh, "/token/refresh")
    api.add_resource(UserLogin, "/login")
    api.add_resource(UserRegistration, "/registration")

    return api
