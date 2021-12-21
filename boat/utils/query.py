from orator.query.builder import QueryBuilder

from boat.utils.field import Field


__all__ = ('Query',)


class Query:
    def select(self, *args: Field, **kwargs):
        def build(builder: QueryBuilder):
            for f in args:
                builder.add_select(f.get_field_name())

        return build

    def join(self, *args): pass
    def where(self, *args): pass
    def having(self, *args): pass
    def group_by(self, *args): pass
    def order_by(self, *args): pass

    def insert(self, *args, **kwargs): pass
    def update(self, *args, **kwargs): pass
    def delete(self, *args, **kwargs): pass
