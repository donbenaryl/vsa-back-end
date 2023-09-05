from src.app.leads.schemas import ILeads, IEmail
from src.config.db import get_db
from src.config.logger import logger
from src.app.leads.models import Emails, Leads
import smtplib
from email.message import EmailMessage

from flask import jsonify, make_response


def get_leads():
    db = next(get_db())
    contents = db.query(Leads).all()
    
    # EMAIL NOT FOUND
    if len(contents) == 0:
        return make_response(jsonify({
            "msg": "No data found"
        }), 404) 

    contentsArr = []
    for content in contents:
        contentsArr.append(content.toDict()) 

    return contentsArr

def insert_leads(body: IEmail):
    print(body)
    # INSERT NEW DATA
    db = next(get_db())
    to_save = {
        "email": body.email,
        "name": body.name,
        "company_name": body.company_name,
        "contact_number": body.contact_number,
        "subject": body.subject,
        "body": body.body,
        "sent_to": body.sent_to
    }
    
    db.add(Emails(**dict(to_save)))

    leads = db.query(Leads).filter(
        Leads.email == body.email,
        Leads.name == body.name,
        Leads.company_name == body.company_name,
        Leads.contact_number == body.contact_number
    ).all()

    # SAVE LEADS IF IT DOES NOT EXIST
    if len(leads) == 0:
        to_save = {
            "email": body.email,
            "name": body.name,
            "company_name": body.company_name,
            "contact_number": body.contact_number
        }
        
        db.add(Leads(**dict(to_save)))
        
    db.commit()

    send_email(body)
        

    return ('', 204)


def send_email(body: IEmail):
    logger.info("Setting SMTP...")

    msg = EmailMessage()
    msg["Subject"] = body.subject
    msg["From"] = body.email
    msg["To"] = "info@azie-don.com"
    msg.set_content(body.body)
    server = smtplib.SMTP_SSL("azie-don.com", 465)

    logger.info("Logging in...")
    server.login("info@azie-don.com", "P@ssw0rd123!")

    logger.info("Sending email...")
    server.send_message(msg)
    server.quit()

    logger.info("Mail sent!")