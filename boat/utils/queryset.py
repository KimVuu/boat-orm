from typing import Union, Tuple, Generator

from boat.utils.model import WhereClause


__all__ = ('Q', 'And', 'Or',)


QueryArgs = Union[WhereClause, "Q"]


class Q:
    def __init__(self, *args: QueryArgs, has:  str = 'AND'):
        self.children: Tuple[QueryArgs] = args
        self.has: str = has

    def __and__(self, other: QueryArgs):
        return self.And(self, other)

    def __iand__(self, other: QueryArgs):
        return self.And(self, other)

    def __or__(self, other: QueryArgs):
        return self.Or(self, other)

    def __ior__(self, other: QueryArgs):
        return self.Or(self, other)

    def add(self, *args: QueryArgs):
        self.children: Tuple[QueryArgs] = self.children + args

    def flat(self) -> Generator[QueryArgs]:
        for q in self.children:
            yield q

    @classmethod
    def And(cls, *args):
        return cls(*args)

    @classmethod
    def Or(cls, *args):
        return cls(*args, has='OR')


And = Q.And
Or = Q.Or
