from models.user import users as UserModel
from helpers.helper import handler_response, jwt_secret
from bcrypt import hashpw, gensalt
from jwt import encode


class users:
    def add_user(self, user, app):
        try:
            pwd = hashpw(user.pwd.encode('utf-8'), gensalt())
            UserModel.insert({
                'username': user.username,
                'pwd': pwd.decode('utf-8'),
                'nombre': user.nombre,
                'apellido': user.apellido,
                'edad': user.edad,
                'cargo' : user.cargo
            })
            return handler_response(app, 201, f'Se creo el usuario {user.username}')
        except Exception as e:
            return handler_response(app, 500, str(e))

    def login(self, user, app):
        try:
            user_found = UserModel.where_username(user.username).first()

            if user_found and user_found.password_valid(user.pwd):
                token = encode(user_found.serialize(), jwt_secret(), algorithm='HS256')
                response = {
                    'token': token,
                    'user': user_found.serialize()
                }
                return handler_response(app, 200, 'Logeado con exito', response)
            message = f'el usuario : {user.username} y/o la contraseña es incorrecta'
            return handler_response(app, 401, message)
        except Exception as error:
            return handler_response(app, 500, str(error))