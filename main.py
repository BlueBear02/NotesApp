from fastapi import FastAPI, HTTPException, Depends, Header
from sqlalchemy.orm import Session
import os
from dotenv import load_dotenv
import crud
import schemas
from database import get_db

load_dotenv()

app = FastAPI(title="Notes App", description="A simple notes management API")

API_KEY = os.getenv("API_KEY")

def verify_api_key(x_api_key: str = Header()):
    if x_api_key != API_KEY:
        raise HTTPException(status_code=403, detail="Invalid API Key")
    return x_api_key


@app.post("/notes")
def create_note(note: schemas.NoteCreate, db: Session = Depends(get_db), api_key: str = Depends(verify_api_key)):
    return crud.create_note(db=db, title=note.title, content=note.content)


@app.get("/notes")
def get_notes(skip: int = 0, limit: int = 100, db: Session = Depends(get_db), api_key: str = Depends(verify_api_key)):
    return crud.get_notes(db, skip=skip, limit=limit)


@app.get("/notes/{note_id}")
def get_note(note_id: int, db: Session = Depends(get_db), api_key: str = Depends(verify_api_key)):
    db_note = crud.get_note(db, note_id=note_id)
    if db_note is None:
        raise HTTPException(status_code=404, detail="Note not found")
    return db_note


@app.put("/notes/{note_id}")
def update_note(note_id: int, note: schemas.NoteUpdate, db: Session = Depends(get_db), api_key: str = Depends(verify_api_key)):
    db_note = crud.update_note(db, note_id=note_id, title=note.title, content=note.content)
    if db_note is None:
        raise HTTPException(status_code=404, detail="Note not found")
    return db_note


@app.delete("/notes/{note_id}")
def delete_note(note_id: int, db: Session = Depends(get_db), api_key: str = Depends(verify_api_key)):
    db_note = crud.delete_note(db, note_id=note_id)
    if db_note is None:
        raise HTTPException(status_code=404, detail="Note not found")
    return db_note
