from pydantic import BaseModel
from typing import Optional, List

# Схемы для Категорий
class CategoryBase(BaseModel):
    title: str

class CategoryCreate(CategoryBase):
    pass

class Category(CategoryBase):
    id: int

    class Config:
        from_attributes = True # Аналог orm_mode в Pydantic v2

# Схемы для Книг
class BookBase(BaseModel):
    title: str
    description: Optional[str] = None
    price: float
    url: Optional[str] = ""
    category_id: int

class BookCreate(BookBase):
    pass

class Book(BookBase):
    id: int

    class Config:
        from_attributes = True