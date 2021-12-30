from orator.query.expression import QueryExpression
from orator.support.grammar import Grammar

__all__ = ('RawSQL', 'OuterRef',)


grammar = Grammar()


class RawSQL(QueryExpression):
    pass


class OuterRef(QueryExpression):
    def get_value(self):
        return grammar.wrap(self._value)
