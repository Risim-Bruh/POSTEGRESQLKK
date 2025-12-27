from app.db.db import engine, Base, SessionLocal
from app.db import crud, models
from fastapi import FastAPI
from app.db import models  # Важно импортировать модели здесь, чтобы Base их "увидел"
from app.api import categories, books

# Эта строка создаст таблицы, используя Base и импортированные модели
Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(categories.router)
app.include_router(books.router)

def main():
    db = SessionLocal()
    print("--- Список категорий ---")
    categories = crud.get_categories(db)
    for cat in categories:
        print(f"ID: {cat.id} | Название: {cat.title}")

    print("\n--- Список книг ---")
    books = crud.get_books(db)
    for book in books:
        print(f"Книга: {book.title} | Цена: {book.price} | Категория ID: {book.category_id}")
    db.close()

if __name__ == "__main__":
    main()

# Создаем таблицы при старте (если их еще нет)
Base.metadata.create_all(bind=engine)

app = FastAPI(title="Octagon Book Store API")

# Подключаем роутеры
app.include_router(categories.router)
# app.include_router(books.router) # Раскомментируйте, когда создадите файл

@app.get("/health")
def health_check():
    return {"status": "alive", "database": "connected"}

app = FastAPI()

app.include_router(categories.router)
app.include_router(books.router) # Теперь книги видны в Swagger

@app.get("/health")
def health():
    return {"status": "ok"}