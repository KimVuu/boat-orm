from contextlib import contextmanager
from typing import Callable, ContextManager

from orator import DatabaseManager


__all__ = ('DatabaseManager', 'Database', 'Transaction')


class Database:
    def __init__(self, db: DatabaseManager):
        self.db: DatabaseManager = db

    def __call__(self, *args, **kwargs) -> DatabaseManager:
        return self.db


class Transaction:
    @contextmanager
    def __call__(self, *args, **kwargs) -> ContextManager[Callable[[], DatabaseManager]]:
        database: Database = Database(db)
        database().begin_transaction()

        try:
            yield database
        except Exception as e:
            database().rollback()
            raise

        try:
            database().commit()
        except Exception:
            database().rollback()
            raise


transaction: Transaction = Transaction()
