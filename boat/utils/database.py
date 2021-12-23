from contextlib import contextmanager
from typing import Callable, ContextManager

from orator import DatabaseManager
from orator.query.builder import QueryBuilder

from boat.utils.dao import DAO


__all__ = ('DatabaseManager', 'Database', 'Transaction')


class Database:
    def __init__(self, db: DatabaseManager):
        self.db: DatabaseManager = db

    def __call__(self, dao: DAO) -> QueryBuilder:
        return dao(db=self.db)


class Transaction:
    def __init__(self, db: DatabaseManager):
        self.db: DatabaseManager = db

    @contextmanager
    def __call__(self) -> ContextManager[Callable[[DAO], QueryBuilder]]:
        self.db.begin_transaction()
        database: Database = Database(self.db)

        try:
            yield database
        except Exception as e:
            database.db.rollback()
            raise

        try:
            database.db.commit()
        except Exception:
            database.db.rollback()
            raise
