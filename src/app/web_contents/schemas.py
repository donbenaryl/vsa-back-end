from pydantic import BaseModel, EmailStr

class IBasicDetailUpdateData(BaseModel):
    col_name: str
    content: str

class IPageDetails(BaseModel):
    id: int
    title: str
    description: str
    img: str or None = None
    location: str or None = None
    page_module: int