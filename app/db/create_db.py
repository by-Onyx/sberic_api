import importlib
import os
from datetime import datetime, timedelta

from sqlalchemy import inspect

from app.db.models.character import Character
from app.db.models.character_clothes import CharacterClothes
from app.db.models.character_type import CharacterType
from app.db.models.clothes import Clothes
from app.db.models.clothes_type import ClothesType
from app.db.models.location import Location
from app.db.models.location_type import LocationType
from app.db.models.transaction_type import TransactionType
from app.db.models.user import User
from app.db.models.user_character import UserCharacter
from app.db.models.user_clothes import UserClothes
from app.db.models.user_location import UserLocation
from app.db.models.user_transactions import UserTransactions
from app.db.database import engine, Base, SessionLocal


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
    date_now = datetime.now()

    initial_data = [
        TransactionType(
            id=1,
            name='Replenishment'
        ),
        TransactionType(
            id=2,
            name='Purchase'
        ),
        TransactionType(
            id=3,
            name='Withdrawal'
        )
    ]
    db.add_all(initial_data)
    db.commit()
    print("Добавлены начальные данные для таблицы TransactionType.")

    initial_data = [
        LocationType(
            id=1,
            name='Ground'
        ),
        LocationType(
            id=2,
            name='Underwater'
        ),
        LocationType(
            id=3,
            name='Aerial'
        ),
        LocationType(
            id=4,
            name='Space'
        )
    ]
    db.add_all(initial_data)
    db.commit()
    print("Добавлены начальные данные для таблицы LocationType.")

    initial_data = [
        CharacterType(
            id=1,
            name='Gopher'
        )
    ]
    db.add_all(initial_data)
    db.commit()
    print("Добавлены начальные данные для таблицы CharacterType.")

    initial_data = [
        ClothesType(
            id=1,
            name='hat'
        ),
        ClothesType(
            id=2,
            name='shirt'
        ),
        ClothesType(
            id=3,
            name='pants'
        )
    ]
    db.add_all(initial_data)
    db.commit()
    print("Добавлены начальные данные для таблицы ClothesType.")

    initial_data = [
        Location(
            id=1,
            name='База',
            price=0,
            file_name='base_location.jpg',
            type_id=1
        )
    ]
    db.add_all(initial_data)
    db.commit()
    print("Добавлены начальные данные для таблицы Location.")

    initial_data = [
        Character(
            id=1,
            name='Сусел',
            character_type_id=1,
            happiness_percent=70
        )
    ]
    db.add_all(initial_data)
    db.commit()
    print("Добавлены начальные данные для таблицы Character.")

    initial_data = [
        Clothes(
            id=1,
            name='Base hat',
            price=150.00,
            file_name='base_hat.jpg',
            clothes_type_id=1
        ),
        Clothes(
            id=2,
            name='Base shirt',
            price=499.99,
            file_name='base_shirt.jpg',
            clothes_type_id=2
        ),
        Clothes(
            id=3,
            name='Base pants',
            price=235.99,
            file_name='base_pants.jpg',
            clothes_type_id=3
        )
    ]
    db.add_all(initial_data)
    db.commit()
    print("Добавлены начальные данные для таблицы Clothes.")

    initial_data = [
        User(
            id=1,
            login='by_Onyx',
            password='',
            age=21,
            balance=4114.02,
            creation_date=date_now
        )
    ]
    db.add_all(initial_data)
    db.commit()
    print("Добавлены начальные данные для таблицы User.")

    initial_data = [
        UserCharacter(
            user_id=1,
            character_id=1
        )
    ]
    db.add_all(initial_data)
    db.commit()
    print("Добавлены начальные данные для таблицы UserCharacter.")

    initial_data = [
        UserLocation(
            user_id=1,
            location_id=1
        )
    ]
    db.add_all(initial_data)
    db.commit()
    print("Добавлены начальные данные для таблицы UserLocation.")

    initial_data = [
        UserClothes(
            user_id=1,
            clothes_id=1
        ),
        UserClothes(
            user_id=1,
            clothes_id=2
        ),
        UserClothes(
            user_id=1,
            clothes_id=3
        )
    ]
    db.add_all(initial_data)
    db.commit()
    print("Добавлены начальные данные для таблицы UserClothes.")

    initial_data = [
        CharacterClothes(
            character_id=1,
            clothes_id=1
        ),
        CharacterClothes(
            character_id=1,
            clothes_id=2
        ),
        CharacterClothes(
            character_id=1,
            clothes_id=3
        )
    ]
    db.add_all(initial_data)
    db.commit()
    print("Добавлены начальные данные для таблицы Character_Clothes.")

    initial_data = [
        UserTransactions(
            user_id=1,
            transfer_amount=5000,
            transaction_type_id=1,
            datetime=date_now
        ),
        UserTransactions(
            user_id=1,
            transfer_amount=499.99,
            transaction_type_id=2,
            datetime=date_now
        ),
        UserTransactions(
            user_id=1,
            transfer_amount=150.00,
            transaction_type_id=2,
            datetime=date_now + timedelta(minutes=2)
        ),
        UserTransactions(
            user_id=1,
            transfer_amount=235.99,
            transaction_type_id=2,
            datetime=date_now + timedelta(minutes=3)
        )
    ]
    db.add_all(initial_data)
    db.commit()
    print("Добавлены начальные данные для таблицы UserTransactions.")


def create_all_tables():
    import_entities()
    db = SessionLocal()
    inspector = inspect(engine)
    all_empty = True
    for table in Base.metadata.sorted_tables:
        if not inspector.has_table(table.name):
            print(f"Создание таблицы {table.name}...")
            Base.metadata.create_all(bind=engine, tables=[table])
        else:
            all_empty = False

    if all_empty:
        add_initial_data(db)

    db.commit()
    db.close()


if __name__ == "__main__":
    create_all_tables()
