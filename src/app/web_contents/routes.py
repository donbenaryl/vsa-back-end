from flask import Blueprint, request, jsonify, make_response
from flask_pydantic import validate
from src.app.auth.services import process_login, process_registration

from src.app.auth.schemas import IUserBasicDetails, INewUserData


auth = Blueprint('auth', __name__)

# @simple_page.route('/', defaults={'page': 'index'})
# @simple_page.route('/<page>')
@auth.route('/login', methods=["POST"])
@validate()
def login(body: IUserBasicDetails):
    return process_login(body)


@auth.route('/register', methods=["POST"])
@validate()
def register(body: INewUserData):
    return process_registration(body)
    # print(data)
    # return "registered!"
    # return ('', 204)


# @auth.route("/token", methods=["POST"])
# def login_for_access_token(
#     form_data: OAuth2PasswordRequestForm = Depends(),
#     db: Session = Depends(get_db),
#     remember_me: bool = False
# ):
#     access_token = login_user(form_data, db, remember_me)
#     return access_token