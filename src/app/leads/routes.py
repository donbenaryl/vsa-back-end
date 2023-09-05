from flask import Blueprint, request
from flask_pydantic import validate
from src.app.leads.services import get_leads, insert_leads
from src.app.leads.schemas import ILeads, IEmail


leads = Blueprint('leads', __name__)


@leads.route('', methods=["GET"])
@validate()
def all_leads():
    return get_leads()


@leads.route('', methods=["POST"])
@validate()
def save_leads(body: IEmail):
    return insert_leads(body)

