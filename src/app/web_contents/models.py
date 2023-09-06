from sqlalchemy import Column, Integer, String, DateTime, inspect
from sqlalchemy.sql import func
import datetime
from src.config.db import Base

class BasicDetails(Base):
    __tablename__ = 'v_basic_details'
    col_name = Column(String, primary_key = True)
    title = Column(String(150))
    content = Column(String)
    order = Column(Integer)

    class Config:
        orm_mode = True

    def serialize(self):
        return {c: getattr(self, c) for c in inspect(self).attrs.keys()}

    @staticmethod
    def serialize_list(l):
        return [m.serialize() for m in l]

    def toDict(self):
        return { c.key: getattr(self, c.key) for c in inspect(self).mapper.column_attrs }

    def __repr__(self):
        return '<Basic Details %r>' % (self.col_name)


class BasicDetailsInDb(BasicDetails):
    last_updated_by = Column(Integer())
    created_at = Column(DateTime(timezone=True), default=func.now())
    updated_at = Column(DateTime(timezone=True), default=func.now(), onupdate=func.now())

    class Config:
        orm_mode = True

    def toDict(self):
        return { c.key: getattr(self, c.key) for c in inspect(self).mapper.column_attrs }

    def __repr__(self):
        return '<Basic Details %r>' % (self.col_name)

class PageDetails(Base):
    __tablename__ = 'v_page_details'
    id = Column(Integer, primary_key = True)
    title = Column(String(250))
    description = Column(String)
    img = Column(String)
    location = Column(String)
    page_module = Column(Integer)

    class Config:
        orm_mode = True

    def serialize(self):
        return {c: getattr(self, c) for c in inspect(self).attrs.keys()}

    @staticmethod
    def serialize_list(l):
        return [m.serialize() for m in l]

    def toDict(self):
        return { c.key: getattr(self, c.key) for c in inspect(self).mapper.column_attrs }

    def __repr__(self):
        return '<Goal %r>' % (self.id)


class PageDetailsInDb(PageDetails):
    last_updated_by = Column(Integer())
    created_at = Column(DateTime(timezone=True), default=func.now())
    updated_at = Column(DateTime(timezone=True), default=func.now(), onupdate=func.now())

    class Config:
        orm_mode = True

    def toDict(self):
        return { c.key: getattr(self, c.key) for c in inspect(self).mapper.column_attrs }

    def __repr__(self):
        return '<Goal %r>' % (self.col_name)