from fastapi import FastAPI,Depends
from database import SessionLocal
from models import Book
from schema import BookDetail
from sqlalchemy.orm import Session

app = FastAPI()

#dependency injection
def get_db():
    db = SessionLocal()
    try:
        yield db

    finally:
        db.close()
        

@app.get("/books")
def all_books(db: Session=Depends(get_db)):
    books = db.query(Book).all()
    return books

@app.post("/add-book")
def add_book(book:BookDetail, db:Session=(get_db)):

    new_book = Book(
        name = book.name,
        genre =book.genre,
        pages = book.pages
    )

    db.add(new_book)
    db.commit()