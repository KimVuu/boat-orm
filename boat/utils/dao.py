from orator import DatabaseManager
from orator.query.builder import QueryBuilder

from boat.utils.model import Model


__all__ = ('DAO',)


class DAO:
    __model__: Model

    def __init__(self, *args):
        self.args = args

    def __call__(self, **kwargs) -> QueryBuilder:
        database: DatabaseManager = kwargs.pop('db')
        builder: QueryBuilder = database.table(self.__model__.__table_name__)
        for sql_func in self.args:
            sql_func(builder)
        return builder
