from fastapi import FastAPI, HTTPException,Depends
from pydantic import BaseModel
from typing import List,Annotated
import model
from database import engine,SessionLocal
from sqlalchemy.orm import Session

app = FastAPI()

class ChoiceBase(BaseModel):
    choice_text:str
    is_correct :bool

class QuestionBase(BaseModel):
    question_text: str
    choices: List[ChoiceBase]

def get_db():
    db = SessionLocal()
    try:
        yield db

    finally:
        db.close()

db_dependency = Annotated(Session, Depends(get_db))

@app.post("/questions/")
async def create_questions(question:QuestionBase, db:db_dependency):
    db_question = model.Questions(question_text=question.question_text)

