from src.app.auth.schemas import IUserBasicDetails, INewUserData
from src.config.db import get_db
from src.app.auth.models import User, UserInDB
from datetime import datetime, timedelta

from flask import jsonify, make_response
import cryptocode
from jose import jwt

USER_KEY = "0x66dFA4b56678B6EdE0ab2765804EeB009dc0EE47"
SECRET_KEY = "12da3c99a9c42c33347b67e452af5e8b9bad81bc4fbfb777af9749cbc6e5399d"

def process_login(data: IUserBasicDetails):
    db = next(get_db())
    user = db.query(UserInDB).filter(UserInDB.email == data.email).first()
    
    # EMAIL NOT FOUND
    if not user:
        return make_response(jsonify({
            "msg": "Invalid username or password"
        }), 404) 

    # INVALID PASSWORD
    if data.password != cryptocode.decrypt(user.password, USER_KEY):
        return make_response(jsonify({
            "msg": "Invalid username or password"
        }), 404) 


    to_encode = {
        "email": data.email,
        "exp": datetime.utcnow() + timedelta(minutes = 0)
    }

    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm="HS256")

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
        "password": cryptocode.encrypt(data.password, USER_KEY),
        "email": data.email
    }
    
    db.add(UserInDB(**dict(to_save)))
    db.commit()

    return ("", 204)