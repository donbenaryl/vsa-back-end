from flask import Flask, request, jsonify, make_response
from flask_cors import CORS
from sqlalchemy import Column, Integer, String, TIMESTAMP, inspect, create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from datetime import datetime, timedelta
import cryptocode
from jose import JWTError, jwt

from src.config.envConfig import CORS

app = Flask(__name__)
CORS(app)
# cors = CORS(app, resources={r"/api": {"origins": "http://localhost:4200"}})
# cors = CORS(app, resources={r"/api/*": {"origins": "*"}})
# cors = CORS(app, resource={
#     r"/*":{
#         "origins":"*"
#     }
# })
# app = CORS(app, resources={r"/api/*": {"origins": ["http://localhost:4200", "http://www.domain2.com"]}})

# cors = CORS(app, origins=['http://localhost:4200', 'http://192.168.1.163:4200'])
# app.config['CORS_HEADERS'] = 'Content-Type'
@app.route("/")
def test_if_working():
    return "It is working kadi!!!"