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
