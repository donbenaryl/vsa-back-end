from flask import Flask, make_response, jsonify, abort, request
from flask_cors import CORS

from src.config.envConfig import DB
from src.app.auth.routes import auth
from src.app.auth.services import get_current_user
from src.app.web_contents.routes import web_contents
from src.app.leads.routes import leads
# from src.app.web_contents.routes import web_contents

app = Flask(__name__)
app.config['SQLALCHEMY_POOL_RECYCLE'] = 28800 - 1
app.register_blueprint(auth, url_prefix='/auth')
app.register_blueprint(web_contents, url_prefix='/web-contents')
app.register_blueprint(leads, url_prefix='/leads')
# CORS(app)
# cors = CORS(app, resources={r"/api": {"origins": "http://localhost:4200"}})
# cors = CORS(app, resources={r"/api/*": {"origins": "*"}})
cors = CORS(app, resources={r"/*": {"origins": ("http://localhost:4200", "http://vsa-be.azie-don.com","http://vsa-test.azie-don.com")}})
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
    return "Hi Hello Good Morning!"


@app.before_request 
def before_request_callback(): 
    requires_login = {
        "auth.register": "POST",
        "auth.user.me": "POST",
        "web-contents.basic-details": "POST",
        "web-contents.goals": "POST",
        "web-contents.services": "POST",
        "web-contents.why-us": "POST",
        "web-contents.why-our-services": "POST",
        "web-contents.our-team": "POST",
        "web-contents.career": "POST",
        "web-contents.goals": "POST",
    }

    if request.method != 'OPTIONS':
        if request.endpoint in requires_login and requires_login[request.endpoint] == request.method:
        # if request.endpoint not in pages_with_auth:
            user = get_current_user()
            
            if user.status_code != 200:
                return user