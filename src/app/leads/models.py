from sqlalchemy import Column, Integer, String, DateTime, inspect
from sqlalchemy.sql import func
import datetime
from src.config.db import Base

class Emails(Base):
    __tablename__ = 'v_emails'
    id = Column(Integer, primary_key = True)
    email = Column(String(250))
    name = Column(String(250))
    contact_number = Column(String(20))
    company_name = Column(String(250))
    subject = Column(String(250))
    body = Column(String(2000))
    sent_to = Column(String(250))
    class Config:
        orm_mode = True

    def toDict(self):
        return { c.key: getattr(self, c.key) for c in inspect(self).mapper.column_attrs }

    def __repr__(self):
        return '<Email %r>' % (self.col_name)


class EmailsInDb(Emails):
    created_at = Column(DateTime(timezone=True), default=func.now())

    class Config:
        orm_mode = True

    def toDict(self):
        return { c.key: getattr(self, c.key) for c in inspect(self).mapper.column_attrs }

    def __repr__(self):
        return '<Email %r>' % (self.col_name)

class Leads(Base):
    __tablename__ = 'v_leads'
    id = Column(Integer, primary_key = True)
    email = Column(String(250))
    name = Column(String(250))
    contact_number = Column(String(20))
    company_name = Column(String(250))

    class Config:
        orm_mode = True

    def toDict(self):
        return { c.key: getattr(self, c.key) for c in inspect(self).mapper.column_attrs }

    def __repr__(self):
        return '<Lead %r>' % (self.id)


class LeadsInDb(Leads):
    created_at = Column(DateTime(timezone=True), default=func.now())

    class Config:
        orm_mode = True

    def toDict(self):
        return { c.key: getattr(self, c.key) for c in inspect(self).mapper.column_attrs }

    def __repr__(self):
        return '<Lead %r>' % (self.col_name)