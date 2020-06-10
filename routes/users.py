from flask import request
from controllers.user import users
from helpers.helper import token_required
from requests import get

UserController = users()

def user_routes(app):
    @app.route('/users', methods=['POST'])
    @token_required
    def create_user():
        values = request.values
        UserController.username = values.get('username')
        UserController.pwd = values.get('pwd')
        UserController.nombre = values.get('nombre')
        UserController.apellido = values.get('apellido')
        UserController.edad = values.get('edad')
        UserController.cargo = values.get('cargo')
        return UserController.add_user(UserController, app)


    @app.route('/login', methods=['POST'])
    def login():
        # Consumo de api externa
        #response = get('http://google.com.pe')
        #print(response.text)
        values = request.values
        UserController.username = values.get('username')
        UserController.pwd = values.get('pwd')
        return UserController.login(UserController, app)
