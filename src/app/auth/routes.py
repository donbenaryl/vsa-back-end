from flask import Blueprint, request, jsonify, make_response
from flask_pydantic import validate
from src.app.auth.services import process_login, process_registration, get_current_user, get_all_users, update_password

from src.app.auth.schemas import IUserBasicDetails, INewUserData, IChangePasswordParams


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
    return get_current_user()


@auth.route('/users', methods=["GET"])
@validate()
def all_user():
    return get_all_users()


@auth.route('/change-password', methods=["POST"])
@validate()
def set_password(body: IChangePasswordParams):
    return update_password(body)