from orator import DatabaseManager
from orator.query.builder import QueryBuilder

from boat.utils.model import Model


__all__ = ('DAO',)


class DAO:
    __model__: Model

    def __new__(cls, *args, **kwargs) -> QueryBuilder:
        database: DatabaseManager = kwargs.pop('db', db)
        builder: QueryBuilder = database.table(cls.__model__.__table_name__)
        for sql_func in args:
            sql_func(builder)
        return builder
