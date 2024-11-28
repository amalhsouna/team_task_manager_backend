from flask import Blueprint, request, jsonify, abort
from flask_jwt_extended import create_access_token
from apifairy import body, response
from core.schema.create_auth_user_schema import CreateAuthUserSchema
from core.services.user_service import UserService
from . import login_api_blueprint

login_schema = CreateAuthUserSchema()

@login_api_blueprint.route('/login', methods=['POST'])
@body(login_schema)
@response({"access_token": "string"})
def login(data):
    username = data["username"]
    password = data["password"]

    # Simuler l'authentification (remplacez cela par votre logique réelle)
    user = UserService.authenticate_user(username, password)
    if user:
        access_token = create_access_token(identity={"id": user.id, "username": user.username})
        return {"access_token": access_token}
    else:
        abort(401, description="Invalid credentials")
