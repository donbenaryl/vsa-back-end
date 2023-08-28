from typing import List

from pydantic import AnyHttpUrl, BaseModel


class Config(BaseModel):
    API_V1_STR: str = "/api/v1"
    # BACKEND_CORS_ORIGINS is a JSON-formatted list of origins
    # e.g: '["http://localhost", "http://localhost:4200", "http://localhost:3000", \
    # "http://localhost:8080", "http://local.dockertoolbox.tiangolo.com"]'
    BACKEND_CORS_ORIGINS: List[AnyHttpUrl] = ["http://localhost:4200", "http://localhost", "https://terminal.syslit.io","http://localhost:8001"]
    DB_NAME: str = "vsa"
    DB_USERNAME: str = "root"
    DB_PASSWORD: str = ""
    DB_HOST: str = "localhost"
    DB_PORT: int = 3306


settings = Config()
