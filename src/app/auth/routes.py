from flask import Blueprint, render_template, abort
from jinja2 import TemplateNotFound

auth = Blueprint('auth', __name__)

# @simple_page.route('/', defaults={'page': 'index'})
# @simple_page.route('/<page>')
@auth.route('/login', methods=["GET"])
def login():
    return "test!"