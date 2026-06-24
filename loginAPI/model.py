from sqlalchemy import Column,Integer,String
from sqlalchemy.orm import declarative_base
from database import engine
Base = declarative_base()

class User(Base):
    __tablename__ = "password_hashing"

    id = Column(Integer,primary_key=True)
    username = Column(String)
    password = Column(String)
    

Base.metadata.create_all(bind=engine)