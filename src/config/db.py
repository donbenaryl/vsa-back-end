from sqlalchemy import create_engine, MetaData
from sqlalchemy.orm import sessionmaker, declarative_base

from .envConfig import DB

import json
import pydantic.json


def _custom_json_serializer(*args, **kwargs) -> str:
    """
    Encodes json in the same way that pydantic does.
    """
    return json.dumps(*args, default=pydantic.json.pydantic_encoder, **kwargs)

engine=create_engine(f'mysql+pymysql://{DB.USER}:{DB.PASSWORD}@{DB.HOST}:{DB.PORT}/{DB.DATABASE}', pool_size=20, max_overflow=0)
sessionlocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

def get_db():
    db = sessionlocal()
    try:
        yield db
    finally:
        db.close()