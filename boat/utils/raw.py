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
