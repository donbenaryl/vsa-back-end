from sqlalchemy import Column, Integer, String, Boolean
from src.config.db import Base

class User(Base):
    __tablename__ = 't_users'
    id = Column(Integer, primary_key = True)
    email = Column(String(150))
    disabled = Column(Boolean)
    user_type = Column(Integer)

    def __repr__(self):
        return '<User %r>' % (self.id)

class UserInDB(User):
    password = Column(String())

    class Config:
        orm_mode = True

    def __repr__(self):
        return '<User %r>' % (self.id)