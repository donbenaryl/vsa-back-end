from .config import settings

class DB:
    PORT = settings.DB_PORT
    USER = settings.DB_USERNAME
    PASSWORD = settings.DB_PASSWORD
    HOST = settings.DB_HOST
    DATABASE = settings.DB_NAME

class USER:
    USER_KEY = settings.USER_KEY
    TOKEN_SECRET_KEY = settings.TOKEN_SECRET_KEY

class CORS:
    BACKEND_CORS_ORIGINS = settings.BACKEND_CORS_ORIGINS