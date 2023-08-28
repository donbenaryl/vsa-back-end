from .config import settings
from src.app.auth.config import auth_config

class DB:
    PORT = settings.DB_PORT
    USER = settings.DB_USERNAME
    PASSWORD = settings.DB_PASSWORD
    HOST = settings.DB_HOST
    DATABASE = settings.DB_NAME

class CORS:
    BACKEND_CORS_ORIGINS = settings.BACKEND_CORS_ORIGINS

class AUTH:
    SECRET_KEY = auth_config.SECRET_KEY
    SGEN_API_KEY = settings.SGEN_API_KEY
    MANAGER_API_KEY = settings.MANAGER_API_KEY