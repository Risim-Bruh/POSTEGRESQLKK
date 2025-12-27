from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from app.db import crud, db
from app import schemas

router = APIRouter(prefix="/books", tags=["books"])

# Получить все книги
@router.get("/", response_model=List[schemas.Book])
def read_books(database: Session = Depends(db.get_db)):
    books = crud.get_books(database)
    return books

# Создать новую книгу
@router.post("/", response_model=schemas.Book, status_code=201)
def create_book(book: schemas.BookCreate, database: Session = Depends(db.get_db)):
    # Валидация: проверяем, существует ли такая категория
    # Для этого в crud.py желательно иметь функцию get_category(db, category_id)
    return crud.create_book(
        database, 
        title=book.title, 
        description=book.description, 
        price=book.price, 
        category_id=book.category_id
    )

# Получить одну книгу по ID
@router.get("/{book_id}", response_model=schemas.Book)
def read_book(book_id: int, database: Session = Depends(db.get_db)):
    # Здесь мы ищем книгу напрямую через SQLAlchemy
    from app.db import models
    db_book = database.query(models.Book).filter(models.Book.id == book_id).first()
    if db_book is None:
        raise HTTPException(status_code=404, detail="Книга не найдена")
    return db_book