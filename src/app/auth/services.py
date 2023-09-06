from src.app.auth.schemas import IUserBasicDetails, INewUserData
from src.config.db import get_db
from src.app.auth.models import User, UserInDB
from datetime import datetime, timedelta
from src.config.envConfig import USER
from src.config.logger import logger

from flask import jsonify, make_response, request
from jose import jwt, JWTError
import base64
from Crypto.Cipher import AES


KEY = bytes(USER.USER_KEY, encoding="raw_unicode_escape")
cipher = AES.new(KEY, AES.MODE_ECB)


def encode_string(string: str):
    password = bytes(string, encoding="raw_unicode_escape").rjust(32)
    return base64.b64encode(cipher.encrypt(password))


def decode_string(string):
    encoded_password = bytes(string, encoding="raw_unicode_escape").rjust(32)
    return str(cipher.decrypt(base64.b64decode(encoded_password)), 'utf-8').strip()


def process_login(data: IUserBasicDetails):
    db = next(get_db())

    logger.info(f"Looking if user {data.email} exists...")
    user = db.query(UserInDB).filter(UserInDB.email == data.email).first()
    
    # EMAIL NOT FOUND
    if not user:
        return make_response(jsonify({
            "msg": "Invalid username or password"
        }), 404)

    # encoded = encode_string(data.password)
    # encoded = str(encoded, 'utf-8').strip()
    # print("encoded", encoded)

    # decoded = decode_string(encoded)
    # print("decoded", decoded)
    
    # INVALID PASSWORD
    if data.password != decode_string(user.password):
        return make_response(jsonify({
            "msg": "Invalid username or password"
        }), 404) 

    logger.info(f"Encoding user {data.email}...")
    to_encode = {
        "email": data.email,
        "exp": datetime.utcnow() + timedelta(minutes = 1000)
    }

    encoded_jwt = jwt.encode(to_encode, USER.TOKEN_SECRET_KEY, algorithm="HS256")

    return make_response(jsonify({
        "token": encoded_jwt
    }), 200)


def process_registration(data: INewUserData):
    # PASSWORD DOES NOT MATCH
    if data.password != data.re_password:
        return make_response(jsonify({
            "msg": "Password does not match"
        }), 400)

    db = next(get_db())
    user = db.query(User).filter(User.email == data.email).first()

    # USER ALREADY EXISTS
    if user:
        return make_response(jsonify({
            "msg": "User already exist!"
        }), 409) 
    
    # INSERT USER
    to_save = {
        "password": encode_string(data.password),
        "email": data.email
    }
    
    db.add(UserInDB(**dict(to_save)))
    db.commit()

    return ("", 204)


def get_current_user():
    try:
        headers = request.headers
        bearer = headers.get('Authorization')
        # print("email22email22email22email22", bearer)
        auth_header = request.headers.get("Authorization")

        if "Bearer" in auth_header:
            token = auth_header.split(' ')[1]
            payload = jwt.decode(token, USER.TOKEN_SECRET_KEY, algorithms = "HS256")

            if payload:
                email: str = payload.get("email")

                return make_response(jsonify({
                    "email": email
                }), 200)
            else:
                return make_response(jsonify({
                    "msg": "Unauthorized User"
                }), 401)  
        
        return make_response(jsonify({
            "msg": "Unauthorized User"
        }), 401)

    except Exception as err:
        print(err)
        return make_response(jsonify({
            "msg": "Unauthorized User"
        }), 401)


# def check_authentication(): 
#     user = get_current_user()
#     print("user", user.json)
    
#     if user.status_code != 200:
#         return user