from flask import Blueprint, request
from flask_pydantic import validate
from src.app.web_contents.services import get_basic_details, update_basic_details, get_page_details, update_page_details, get_page_detail
from src.app.web_contents.schemas import IBasicDetailUpdateData, IPageDetails


web_contents = Blueprint('web_contents', __name__)


@web_contents.route('/basic-details', methods=["GET"])
@validate()
def basic_details():
    return get_basic_details()


@web_contents.route('/basic-details', methods=["POST"])
@validate()
def set_basic_details(body: IBasicDetailUpdateData):
    return update_basic_details(body)


@web_contents.route('/goals', methods=["GET"])
@validate()
def goals():
    return get_page_details(1)


@web_contents.route('/goals', methods=["POST"])
@validate()
def set_goals():
    data: list[IPageDetails] = request.get_json()
    return update_page_details(data, 1)


@web_contents.route('/services', methods=["GET"])
@validate()
def services():
    return get_page_details(2)


@web_contents.route('/services', methods=["POST"])
@validate()
def set_services():
    data: list[IPageDetails] = request.get_json()
    return update_page_details(data, 2)


@web_contents.route('/why-us', methods=["GET"])
@validate()
def why_us():
    return get_page_details(3)


@web_contents.route('/why-us', methods=["POST"])
@validate()
def set_why_us():
    data: list[IPageDetails] = request.get_json()
    return update_page_details(data, 3)


@web_contents.route('/why-our-services', methods=["GET"])
@validate()
def why_our_services():
    return get_page_details(4)


@web_contents.route('/why-our-services', methods=["POST"])
@validate()
def set_why_our_services():
    data: list[IPageDetails] = request.get_json()
    return update_page_details(data, 4)


@web_contents.route('/our-team', methods=["GET"])
@validate()
def our_team():
    return get_page_details(5)



@web_contents.route('/our-team', methods=["POST"])
@validate()
def set_our_team():
    data: list[IPageDetails] = request.get_json()
    return update_page_details(data, 5)


@web_contents.route('/careers', methods=["GET"])
@validate()
def careers():
    return get_page_details(6)


@web_contents.route('/careers/<id>', methods=["GET"])
@validate()
def career(id):
    return get_page_detail(id)



@web_contents.route('/careers', methods=["POST"])
@validate()
def set_careers():
    data: list[IPageDetails] = request.get_json()
    return update_page_details(data, 6)



