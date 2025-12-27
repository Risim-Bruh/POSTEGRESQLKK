from app.db.db import engine, Base, SessionLocal
from app.db import crud, models

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