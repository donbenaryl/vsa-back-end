from flask import Flask
from flask_cors import CORS

from src.config.envConfig import DB
from src.app.auth.routes import auth

app = Flask(__name__)
app.register_blueprint(auth)
# CORS(app)
# cors = CORS(app, resources={r"/api": {"origins": "http://localhost:4200"}})
# cors = CORS(app, resources={r"/api/*": {"origins": "*"}})
cors = CORS(app, resource={
    r"/*":{
        "origins":"*"
    }
})
# app = CORS(app, resources={r"/api/*": {"origins": ["http://localhost:4200", "http://www.domain2.com"]}})

# cors = CORS(app, origins=['http://localhost:4200', 'http://192.168.1.163:4200'])
# app.config['CORS_HEADERS'] = 'Content-Type'
@app.route("/")
def test_if_working():
    return "It is working kadi!!!"