from abc import ABCMeta
from contextlib import contextmanager
from typing import Any, Dict, Tuple, Optional, Callable, ContextManager, Iterable

# from orator import DatabaseManager
# from orator.query.builder import QueryBuilder
# from orator.query.expression import QueryExpression
# from orator.query.grammars.mysql_grammar import MySQLQueryGrammar
#
#
# config = {
#     'mysql': {
#         'driver': 'mysql',
#         'host': '127.0.0.1',
#         'database': 'boat',
#         'user': 'root',
#         'password': 'password',
#     }
# }
# grammar: MySQLQueryGrammar = MySQLQueryGrammar()
# db: DatabaseManager = DatabaseManager(config)
#
#
# class Database:
#     def __init__(self, db: DatabaseManager):
#         self.db: DatabaseManager = db
#
#     def __call__(self, *args, **kwargs) -> DatabaseManager:
#         return self.db
#
#
# class Transaction:
#     @contextmanager
#     def __call__(self, *args, **kwargs) -> ContextManager[Callable[[], DatabaseManager]]:
#         database: Database = Database(db)
#         database().begin_transaction()
#
#         try:
#             yield database
#         except Exception as e:
#             database().rollback()
#             raise
#
#         try:
#             database().commit()
#         except Exception:
#             database().rollback()
#             raise
#
#
# transaction: Transaction = Transaction()
#
#
# class RawSQL(QueryExpression):
#     pass
#
#
# class OuterRef(QueryExpression):
#     def get_value(self):
#         return grammar.wrap(self._value)


class Field:
    def __init__(self, field_name: str, table_name: str = ''):
        self._field_name: str = field_name
        self._table_name: str = table_name

    def get_field_name(self):
        if self._table_name:
            return f"{self._table_name}.{self._field_name}"
        return self._field_name

    def asc(self) -> str: return f"{self.get_field_name()} ASC"
    def desc(self) -> str: return f"{self.get_field_name()} DESC"

    def eq(self, value) -> str: return f"{self.get_field_name()} = {value}"
    def gt(self, value) -> str: return f"{self.get_field_name()} > {value}"
    def gte(self, value) -> str: return f"{self.get_field_name()} >= {value}"
    def lt(self, value) -> str: return f"{self.get_field_name()} < {value}"
    def lte(self, value) -> str: return f"{self.get_field_name()} <= {value}"
    def in_(self, values) -> str: return f"{self.get_field_name()} IN {values}"
    def not_in_(self, values) -> str: return f"{self.get_field_name()} NOT IN {values}"
    def is_null(self) -> str: return f"{self.get_field_name()} IS NULL"
    def is_not_null(self) -> str: return f"{self.get_field_name()} IS NOT NULL"


class FieldDict:
    def __init__(self, table_name: str = ''):
        self._table_name = table_name

    def __getitem__(self, item: str) -> Field:
        return Field(item, table_name=self._table_name)


class FieldDictDecoratorValue(property):
    def __get__(self, instance, owner: "Model") -> FieldDict:
        return FieldDict(table_name=owner.__table_name__)


class Q:
    def __init__(self, *args, has: str = 'AND', is_not: bool = False):
        self.has: str = has
        self.is_not: bool = is_not

    @classmethod
    def And(cls, *args):
        return cls(*args)

    @classmethod
    def Or(cls, *args):
        return cls(*args, has='OR')

    @classmethod
    def Not(cls, *args):
        return cls(*args, is_not=True)


And = Q.And
Or = Q.Or
Not = Q.Not


class Query:
    def select(self, *args, **kwargs): print(args, kwargs)
    def join(self, *args): print(args)
    def where(self, *args): print(args)
    def having(self, *args): print(args)
    def group_by(self, *args): print(args)
    def order_by(self, *args): print(args)

    def insert(self, *args, **kwargs): print(args, kwargs)
    def update(self, *args, **kwargs): print(args, kwargs)
    def delete(self, *args, **kwargs): print(args, kwargs)


class Model:
    __table_name__: str

    @FieldDictDecoratorValue
    def fields(cls):
        pass


class DAO:
    __model__: Model

    def __init__(self, *args):
        pass

    @classmethod
    def from_model(cls, model: Model):
        cls.__model__ = model
        return cls


it: Query = Query()


class SqlValue:
    format: str = '{sql}'

    def __init__(self, value, **kwargs):
        self.value = value
        self.kwargs = kwargs
        self.bindings = kwargs.pop('bindings', [])

    def get_value(self):
        return self.value

    def get_format(self) -> str:
        return self.format

    def get_sql(self) -> str:
        return self.get_format().format(sql=self.get_value(), **self.kwargs)

    def get_bindings(self):
        return self.bindings


class Raw(SqlValue):
    format: str = '{sql} AS {alias}'


class Function(Raw):
    func: str = ''
    sql: str = '{func}({sql})'
    format: str = ' AS {alias}'

    def get_format(self) -> str:
        return self.sql + self.format
    
    def get_sql(self) -> str:
        return self.get_format().format(sql=self.get_value(), func=self.func, **self.kwargs)


field = FieldDict()


class Shop(Model):
    __table_name__: str = 'Shop'


class ShopDAO(DAO.from_model(Shop)):
    pass


ShopDAO(
    it.select(
        Shop.fields['id'],
        Shop.fields['title'],
        Shop.fields['adress'],
        owner_name=Shop.fields['owner'],
    ),
)
