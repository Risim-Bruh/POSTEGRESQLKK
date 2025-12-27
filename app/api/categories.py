from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.db import crud, db
from app import schemas
from typing import List

router = APIRouter(prefix="/categories", tags=["categories"])

@router.get("/", response_model=List[schemas.Category])
def read_categories(database: Session = Depends(db.get_db)):
    return crud.get_categories(database)

@router.post("/", response_model=schemas.Category, status_code=201)
def create_category(category: schemas.CategoryCreate, database: Session = Depends(db.get_db)):
    return crud.create_category(database, title=category.title)