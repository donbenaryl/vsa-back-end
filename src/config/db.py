from sqlalchemy import create_engine, MetaData
from sqlalchemy.orm import sessionmaker, declarative_base

from src.config.logger import logger
from .envConfig import DB


engine=create_engine(f'mysql+pymysql://{DB.USER}:{DB.PASSWORD}@{DB.HOST}:{DB.PORT}/{DB.DATABASE}', pool_size=50, max_overflow=0)
sessionlocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

def get_db():
    db = sessionlocal()
    try:
        logger.info("Opening connection...")
        yield db
    finally:
        db.close()
        logger.info("Connection closed!")