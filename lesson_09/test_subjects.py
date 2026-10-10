from sqlalchemy import text
from db_config import engine


def test_add_subject():
    with engine.connect() as connection:
        transaction = connection.begin()

        try:
            result = connection.execute(
                text(
                    'INSERT INTO "предметы" ("название") '
                    'VALUES (:name) RETURNING id'
                ),
                {"name": "Тестовый предмет"}
            )

            subject_id = result.scalar_one()

            result = connection.execute(
                text(
                    'SELECT "название" FROM "предметы" '
                    'WHERE id = :id'
                ),
                {"id": subject_id}
            )

            assert result.scalar_one() == "Тестовый предмет"

        finally:
            transaction.rollback()


def test_update_subject():
    with engine.connect() as connection:
        transaction = connection.begin()

        try:
            result = connection.execute(
                text(
                    'INSERT INTO "предметы" ("название") '
                    'VALUES (:name) RETURNING id'
                ),
                {"name": "Физика"}
            )

            subject_id = result.scalar_one()

            connection.execute(
                text(
                    'UPDATE "предметы" '
                    'SET "название" = :name '
                    'WHERE id = :id'
                ),
                {"name": "Химия", "id": subject_id}
            )

            result = connection.execute(
                text(
                    'SELECT "название" FROM "предметы" '
                    'WHERE id = :id'
                ),
                {"id": subject_id}
            )

            assert result.scalar_one() == "Химия"

        finally:
            transaction.rollback()


def test_delete_subject():
    with engine.connect() as connection:
        transaction = connection.begin()

        try:
            result = connection.execute(
                text(
                    'INSERT INTO "предметы" ("название") '
                    'VALUES (:name) RETURNING id'
                ),
                {"name": "Биология"}
            )

            subject_id = result.scalar_one()

            connection.execute(
                text(
                    'DELETE FROM "предметы" WHERE id = :id'
                ),
                {"id": subject_id}
            )

            result = connection.execute(
                text(
                    'SELECT id FROM "предметы" WHERE id = :id'
                ),
                {"id": subject_id}
            )

            assert result.scalar_one_or_none() is None

        finally:
            transaction.rollback()
