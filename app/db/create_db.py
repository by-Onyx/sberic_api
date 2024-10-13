import importlib
import os

from sqlalchemy import inspect

from .database import engine, Base, SessionLocal
from .models.character_type import CharacterType
from .models.location_type import LocationType
from .models.transaction_type import TransactionType


def import_entities():
    entities_dir = os.path.join(os.path.dirname(__file__), 'models')
    for file in os.listdir(entities_dir):
        if file.endswith('.py') and file != '__init__.py':
            module_name = f".models.{file[:-3]}"
            try:
                importlib.import_module(module_name, package='app.db')
            except Exception as e:
                print(f"Ошибка при импорте модуля {module_name}: {e}")


def add_initial_data(db):
    """Добавляет начальные данные в таблицы после их создания."""
    if not db.query(TransactionType).first():
        initial_data = [
            TransactionType(name='Replenishment'),
            TransactionType(name='Purchase'),
            TransactionType(name='Withdrawal ')
        ]
        db.add_all(initial_data)
        print("Добавлены начальные данные для таблицы TransactionType.")

    if not db.query(LocationType).first():
        initial_data = [
            LocationType(name='Ground'),
            LocationType(name='Underwater'),
            LocationType(name='Aerial'),
            LocationType(name='Space')
        ]
        db.add_all(initial_data)
        print("Добавлены начальные данные для таблицы LocationType.")

    if not db.query(CharacterType).first():
        initial_data = [
            CharacterType(name='Gopher')
        ]
        db.add_all(initial_data)
        print("Добавлены начальные данные для таблицы CharacterType.")


def create_all_tables():
    import_entities()
    db = SessionLocal()
    inspector = inspect(engine)
    for table in Base.metadata.sorted_tables:
        if not inspector.has_table(table.name):
            print(f"Создание таблицы {table.name}...")
            Base.metadata.create_all(bind=engine, tables=[table])
        else:
            print(f"Таблица {table.name} уже существует.")

    add_initial_data(db)
    db.commit()
    db.close()


if __name__ == "__main__":
    create_all_tables()
