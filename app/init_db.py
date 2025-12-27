from app.db.db import engine, Base, SessionLocal
from app.db import crud, models

# Создаем таблицы
Base.metadata.create_all(bind=engine)

def init():
    db = SessionLocal()
    # Создаем категории
    cat1 = crud.create_category(db, "Программирование")
    cat2 = crud.create_category(db, "Художественная литература")

    # Добавляем книги
    crud.create_book(db, "Чистый код", "Роберт Мартин", 1500.0, cat1.id)
    crud.create_book(db, "Изучаем Python", "Марк Лутц", 2500.0, cat1.id)
    crud.create_book(db, "1984", "Джордж Оруэлл", 500.0, cat2.id)
    crud.create_book(db, "Мастер и Маргарита", "Михаил Булгаков", 700.0, cat2.id)
    
    db.close()
    print("Данные успешно добавлены!")

if __name__ == "__main__":
    init()