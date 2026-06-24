from pydantic import BaseModel

class BookDetail(BaseModel):
    name : str
    genre: str
    pages : str