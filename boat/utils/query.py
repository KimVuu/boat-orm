from typing import Callable, Tuple, Union

from orator.query.builder import QueryBuilder

from boat.utils.model import WhereClause, Field
from boat.utils.queryset import Q


__all__ = ('Query',)


OrderByArgs = Tuple[str, str]
BuildFunction = Callable[[QueryBuilder], None]


class Query:
    def select(self, *args: Field, **kwargs) -> BuildFunction:
        def build(builder: QueryBuilder) -> None:
            for f in args:
                builder.add_select(f.get_field_name())

        return build

    def join(self, *args): pass
    def inner_join(self, *args): pass
    def left_join(self, *args): pass
    def right_join(self, *args): pass
    def full_join(self, *args): pass

    def where(self, *args: Union[WhereClause, Q]):
        wheres = Q(*args)

        def combine(new_query: Callable[[], QueryBuilder], values: Q):
            query = new_query()
            for value in values.flat():
                if isinstance(value, WhereClause):
                    where_type, *values = value.where()
                    query_callable: Callable[[Q], None] = getattr(query, where_type)
                    query_callable(*values)
                elif isinstance(value, Q):
                    data = combine(new_query, value)
                    query.where_nested(data, boolean=value.has)
            return query

        def build(builder: QueryBuilder):
            query = combine(builder.new_query, wheres)
            builder.where_nested(query)

        return build

    def having(self, *args): pass
    def group_by(self, *args): pass

    def order_by(self, *args: OrderByArgs) -> BuildFunction:
        def build(builder: QueryBuilder):
            for field, direction in args:
                builder.order_by(field, direction)

        return build

    def insert(self, *args, **kwargs): pass
    def update(self, *args, **kwargs): pass
    def delete(self, *args, **kwargs): pass
