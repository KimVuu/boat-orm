from typing import Any, List, Dict, Optional


class SqlValue:
    format: str = '{sql}'

    def __init__(self, value: Any, bindings: Optional[List[Any]] = None, **kwargs: Any):
        self.value: Any = value
        self.bindings: List[Any] = bindings
        if self.bindings is None:
            self.bindings: List[Any] = []
        self.kwargs: Dict[str, Any] = kwargs

    def get_value(self) -> Any:
        return self.value

    def get_kwargs(self) -> Dict[str, Any]:
        return self.kwargs

    def get_format(self) -> str:
        return self.format

    def get_sql(self) -> str:
        return self.get_format().format(sql=self.get_value(), **self.get_kwargs())

    def get_bindings(self) -> List[Any]:
        return self.bindings


class Raw(SqlValue):
    format: str = '{sql} AS {alias}'


class Function(SqlValue):
    func: str = ''
    sql: str = '{func}({sql})'
    format: str = ' AS {alias}'

    def get_kwargs(self) -> Dict[str, Any]:
        self.kwargs['func'] = self.func
        return self.kwargs

    def get_format(self) -> str:
        return self.sql + self.format
