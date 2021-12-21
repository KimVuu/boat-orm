from orator.query.expression import QueryExpression


__all__ = ('RawSQL', 'OuterRef',)


class RawSQL(QueryExpression):
    pass


class OuterRef(QueryExpression):
    def get_value(self):
        return grammar.wrap(self._value)
