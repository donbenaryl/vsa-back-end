from sqlalchemy import Column, Integer, String, Boolean
from src.config.db import Base

class User(Base):
    __tablename__ = 'v_users'
    id = Column(Integer, primary_key = True)
    email = Column(String(150))
    # disabled = Column(Boolean)
    # user_type = Column(Integer)

    def __repr__(self):
        return '<User %r>' % (self.id)

# class User(db.Document):   
#     name = db.StringField()
#     password = db.StringField()
#     email = db.StringField()                                                                                                 
#     def to_json(self):        
#         return {"name": self.name,
#                 "email": self.email}

#     def is_authenticated(self):
#         return True

#     def is_active(self):   
#         return True           

#     def is_anonymous(self):
#         return False          

#     def get_id(self):         
#         return str(self.id)

class UserInDB(User):
    password = Column(String())

    class Config:
        orm_mode = True

    def __repr__(self):
        return '<User %r>' % (self.id)