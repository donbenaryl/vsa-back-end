from pydantic import BaseModel, EmailStr

class ILeads(BaseModel):
    id: int or None = None
    email: str
    name: str
    contact_number: str or None = None
    company_name: str or None = None
    subject: str
    body: str

class IEmail(ILeads):
    subject: str
    body: str
    sent_to: str