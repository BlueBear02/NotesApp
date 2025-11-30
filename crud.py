from sqlalchemy.orm import Session
from database import Note
from datetime import datetime

def get_notes(db: Session, skip: int = 0, limit: int = 100,
              category: str = None, is_favourite: bool = None,
              sort_by: str = None, sort_order: str = "desc"):
    query = db.query(Note)

    # Apply filters
    if category is not None:
        query = query.filter(Note.category == category)

    if is_favourite is not None:
        query = query.filter(Note.is_favourite == is_favourite)

    # Apply sorting
    if sort_by == "created":
        if sort_order == "asc":
            query = query.order_by(Note.created_at.asc())
        else:
            query = query.order_by(Note.created_at.desc())
    elif sort_by == "updated":
        if sort_order == "asc":
            query = query.order_by(Note.updated_at.asc())
        else:
            query = query.order_by(Note.updated_at.desc())
    elif sort_by == "category":
        if sort_order == "asc":
            query = query.order_by(Note.category.asc())
        else:
            query = query.order_by(Note.category.desc())
    else:
        # Default: sort by created_at descending (newest first)
        query = query.order_by(Note.created_at.desc())

    return query.offset(skip).limit(limit).all()

def get_note(db: Session, note_id: int):
    return db.query(Note).filter(Note.id == note_id).first()

def create_note(db: Session, title: str, content: str,
                category: str = None, is_favourite: bool = False,
                is_hidden: bool = False):
    db_note = Note(
        title=title,
        content=content,
        category=category,
        is_favourite=is_favourite,
        is_hidden=is_hidden
    )
    db.add(db_note)
    db.commit()
    db.refresh(db_note)
    return db_note

def update_note(db: Session, note_id: int, title: str = None,
                content: str = None, category: str = None,
                is_favourite: bool = None, is_hidden: bool = None):
    db_note = db.query(Note).filter(Note.id == note_id).first()
    if db_note:
        if title is not None:
            db_note.title = title
        if content is not None:
            db_note.content = content
        if category is not None:
            db_note.category = category
        if is_favourite is not None:
            db_note.is_favourite = is_favourite
        if is_hidden is not None:
            db_note.is_hidden = is_hidden
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