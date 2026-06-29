from .config import settings
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


DATABASE_URL = settings.database_url

engine = create_engine(DATABASE_URL)

Session_local = sessionmaker(
        autoflush=False,
        autocommit = False,
        bind=engine
    )

def get_db():
    db = Session_local()

    try:
        yield db

    finally:
        db.close()

    
