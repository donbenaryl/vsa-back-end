from flask import Blueprint, request, jsonify, make_response
from flask_pydantic import validate
from src.app.auth.services import process_login, process_registration, get_current_user

from src.app.auth.schemas import IUserBasicDetails, INewUserData


auth = Blueprint('auth', __name__)


@auth.route('/login', methods=["POST"])
@validate()
def login(body: IUserBasicDetails):
    return process_login(body)


@auth.route('/register', methods=["POST"])
@validate()
def register(body: INewUserData):
    return process_registration(body)


@auth.route('/users/me', methods=["GET"])
@validate()
def current_user():
    headers = request.headers
    bearer = headers.get('Authorization')
    return get_current_user(bearer)