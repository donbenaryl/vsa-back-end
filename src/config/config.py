from typing import List

from pydantic import AnyHttpUrl, BaseModel


class Config(BaseModel):
    API_V1_STR: str = "/api/v1"
    # BACKEND_CORS_ORIGINS is a JSON-formatted list of origins
    # e.g: '["http://localhost", "http://localhost:4200", "http://localhost:3000", \
    # "http://localhost:8080", "http://local.dockertoolbox.tiangolo.com"]'
    BACKEND_CORS_ORIGINS: List[AnyHttpUrl] = ["http://localhost:4200", "http://localhost", "https://terminal.syslit.io","http://localhost:8001"]
    DB_NAME: str = "virtual_staff_avenue"
    DB_USERNAME: str = "don159"
    DB_PASSWORD: str = "NIdb7ft&[mco"
    DB_HOST: str = "localhost"
    DB_PORT: int = 3306
    USER_KEY: str = "0x66dFA4b56678B6"
    TOKEN_SECRET_KEY: str = "12da3c99a9c42c33347b67e452af5e8b9bad81bc4fbfb777af9749cbc6e5399d"


settings = Config()
