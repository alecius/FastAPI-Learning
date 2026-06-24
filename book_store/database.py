from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

DATABASE_URL = "URL"

engine = create_engine(DATABASE_URL)

SessionLocal = sessionmaker(
    autoflush=False,
    autocommit = False,
    bind = engine
)

