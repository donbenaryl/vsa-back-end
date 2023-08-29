from pydantic import BaseModel, EmailStr

class IToken(BaseModel):
    access_token: str
    token_type: str

class ITokenData(BaseModel):
    email: EmailStr or None = None

class IUserBasicDetails(BaseModel):
    email: EmailStr or None = None
    password: str

class IUser(BaseModel):
    email: EmailStr or None = None
    # disabled: bool or None = None
    # user_type: int = 0

    class Config:
        orm_mode = True

class IUserInDb(IUser):
    id: int
    password: str

    class Config:
        orm_mode = True


class IChangePasswordParams(BaseModel):
    user_id: int or None = None
    old_password: str
    new_password: str
    re_password: str


class INewUserData(BaseModel):
    email: EmailStr
    password: str
    re_password: str