from sqlalchemy import Column, Integer, String
from src.config.db import Base

class User(Base):
    __tablename__ = 'v_users'
    id = Column(Integer, primary_key = True)
    email = Column(String(150))

    def __repr__(self):
        return '<User %r>' % (self.id)


class UserInDB(User):
    password = Column(String())

    class Config:
        orm_mode = True

    def __repr__(self):
        return '<User %r>' % (self.id)