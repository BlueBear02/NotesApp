from sqlalchemy.orm import Session
from database import Note
from datetime import datetime

def get_notes(db: Session, skip: int = 0, limit: int = 100):
    return db.query(Note).offset(skip).limit(limit).all()

def get_note(db: Session, note_id: int):
    return db.query(Note).filter(Note.id == note_id).first()

def create_note(db: Session, title: str, content: str):
    db_note = Note(title=title, content=content)
    db.add(db_note)
    db.commit()
    db.refresh(db_note)
    return db_note

def update_note(db: Session, note_id: int, title: str = None, content: str = None):
    db_note = db.query(Note).filter(Note.id == note_id).first()
    if db_note:
        if title is not None:
            db_note.title = title
        if content is not None:
            db_note.content = content
        db_note.updated_at = datetime.utcnow()
        db.commit()
        db.refresh(db_note)
    return db_note

def delete_note(db: Session, note_id: int):
    db_note = db.query(Note).filter(Note.id == note_id).first()
    if db_note:
        db.delete(db_note)
        db.commit()
    return db_note