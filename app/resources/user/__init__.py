from flask_restful import Resource, reqparse
from flask_jwt_extended import create_access_token, create_refresh_token, jwt_required

from app.models.user import UserModel

parser = reqparse.RequestParser()
parser.add_argument("username", help="This field cannot be blank", required=True)
parser.add_argument("password", help="This field cannot be blank", required=True)


class UserRegistration(Resource):
    def post(self):
        data = parser.parse_args()
        new_user = UserModel(
            username=data.get("username"),
            password=UserModel.generate_hash(data.get("password")),
            email=data.get("email"),
        )
        try:
            if UserModel.find_by_username(data.get("username")) or UserModel.find_by_email(data.get("email")):
                return {"message": f"User alread exists"}

            new_user.save_to_db()
            access_token = create_access_token(identity=data.get("username"))
            refresh_token = create_refresh_token(identity=data.get("username"))

            return {
                "message": f"User {data.get('username')} was created",
                "access_token": access_token,
                "refresh_token": refresh_token,
            }

        except:
            return {"message": "Something went wrong"}, 500


class UserLogin(Resource):
    def post(self):
        data = parser.parse_args()
        current_user = UserModel.find_by_username(username=data.get("username"))

        if not current_user:
            return {"message": f"User {data.get('username')} doesnt exists"}

        if UserModel.verify_hash(data.get("password"), current_user.password):
            access_token = create_access_token(identity=data.get("username"))
            refresh_token = create_refresh_token(identity=data.get("username"))

            return {
                "message": f"User {data.get('username')} logged",
                "access_token": access_token,
                "refresh_token": refresh_token,
            }

        else:
            return {"message": "wrong credentials"}
