from typing import Any, Generic, Iterator, Optional, Sequence, Tuple, TypeVar

from orator import DatabaseManager
from orator.query.builder import QueryBuilder

__all__ = (
    'WhereClause', 'Field', 'FieldDict', 'FieldDictDecorator', 'Model', 'DAO',
)


T = TypeVar('T')


class WhereClause:
    def __init__(
        self,
        where_type: str,
        field: str,
        operator: Optional[Any] = None,
        value: Optional[Any] = None,
    ):
        self.where_type: str = where_type
        self.field: str = field
        self.operator: Optional[Any] = operator
        self.value: Optional[Any] = value

    def get(self) -> Tuple[str, str, Optional[Any], Optional[Any]]:
        return self.where_type, self.field, self.operator, self.value

    def filter(self) -> Iterator[Any]:
        return filter(lambda x: x, self.get())

    def where(self) -> Iterator[Any]:
        return self.filter()


class Field(Generic[T]):
    def __init__(self, field_name: str, table_name: str = ''):
        self._field_name: str = field_name
        self._table_name: str = table_name

    def get_field_name(self) -> str:
        if self._table_name:
            return f"{self._table_name}.{self._field_name}"
        return self._field_name

    def asc(self) -> Tuple[str, str]: return self.get_field_name(), "ASC"
    def desc(self) -> Tuple[str, str]: return self.get_field_name(), "DESC"

    def eq(self, value: T) -> WhereClause:
        return WhereClause("where", self.get_field_name(), "=", value)

    def gt(self, value: T) -> WhereClause:
        return WhereClause("where", self.get_field_name(), ">", value)

    def gte(self, value: T) -> WhereClause:
        return WhereClause("where", self.get_field_name(), ">=", value)

    def lt(self, value: T) -> WhereClause:
        return WhereClause("where", self.get_field_name(), "<", value)

    def lte(self, value: T) -> WhereClause:
        return WhereClause("where", self.get_field_name(), "<=", value)

    def in_(self, values: Sequence[T]) -> WhereClause:
        return WhereClause("where_in", self.get_field_name(), values)

    def not_in(self, values: Sequence[T]) -> WhereClause:
        return WhereClause("where_not_in", self.get_field_name(), values)

    def is_null(self) -> WhereClause:
        return WhereClause("where_null", self.get_field_name())

    def is_not_null(self) -> WhereClause:
        return WhereClause("where_not_null", self.get_field_name())


class FieldDict:
    def __init__(self, table_name: str = ''):
        self._table_name = table_name

    def __getitem__(self, item: str) -> Field:
        return Field(item, table_name=self._table_name)


class FieldDictDecorator:
    def __get__(self, instance, owner) -> FieldDict:
        return FieldDict(owner.__table_name__)


class Model:
    __table_name__: str

    fields: FieldDictDecorator = FieldDictDecorator()


class DAO:
    __model__: Model

    def __init__(self, *args):
        self.args = args

    def __call__(self, **kwargs) -> QueryBuilder:
        database: DatabaseManager = kwargs.pop('db')
        builder: QueryBuilder = database.table(self.__model__.__table_name__)
        for sql_func in self.args:
            if sql_func is not None:
                sql_func(builder)
        return builder
