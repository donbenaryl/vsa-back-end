from src.app.auth.schemas import IUserBasicDetails, INewUserData
from src.config.db import get_db
from src.app.auth.models import User, UserInDB
from datetime import datetime, timedelta
from src.config.envConfig import USER

from flask import jsonify, make_response, request
import cryptocode
from jose import jwt, JWTError


def process_login(data: IUserBasicDetails):
    db = next(get_db())
    user = db.query(UserInDB).filter(UserInDB.email == data.email).first()
    
    # EMAIL NOT FOUND
    if not user:
        return make_response(jsonify({
            "msg": "Invalid username or password"
        }), 404) 

    # INVALID PASSWORD
    if data.password != cryptocode.decrypt(user.password, USER.USER_KEY):
        return make_response(jsonify({
            "msg": "Invalid username or password"
        }), 404) 


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
        "password": cryptocode.encrypt(data.password, USER.USER_KEY),
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