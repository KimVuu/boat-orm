from typing import Any, Generator, Tuple, Union

from boat.utils.model import WhereClause

__all__ = ('Q', 'And', 'Or',)


QueryArgs = Union[WhereClause, "Q"]


class Q:
    def __init__(self, *args: QueryArgs, has:  str = 'AND'):
        self.children: Tuple[QueryArgs, ...] = args
        self.has: str = has

    def __and__(self, other: QueryArgs):
        return self.And(self, other)

    def __iand__(self, other: QueryArgs):
        return self.And(self, other)

    def __or__(self, other: QueryArgs):
        return self.Or(self, other)

    def __ior__(self, other: QueryArgs):
        return self.Or(self, other)

    def flat(self) -> Generator[QueryArgs, Any, None]:
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
