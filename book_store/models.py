from sqlalchemy import Column,Integer,String
from sqlalchemy.orm import declarative_base
from database import engine

Base = declarative_base()

class Book(Base):
    __tablename__ = "Books"

    id = Column(Integer,primary_key=True)
    name = Column(String)
    genre = Column(String)
    pages = Column(Integer)

Base.metadata.create_all(bing=engine)