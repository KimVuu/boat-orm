class Field:
    def __init__(self, field_name: str, table_name: str = ''):
        self._field_name: str = field_name
        self._table_name: str = table_name

    def get_field_name(self):
        if self._table_name:
            return f"{self._table_name}.{self._field_name}"
        return self._field_name

    def asc(self) -> str: return f"{self.get_field_name()} ASC"
    def desc(self) -> str: return f"{self.get_field_name()} DESC"

    def eq(self, value) -> str: return f"{self.get_field_name()} = {value}"
    def gt(self, value) -> str: return f"{self.get_field_name()} > {value}"
    def gte(self, value) -> str: return f"{self.get_field_name()} >= {value}"
    def lt(self, value) -> str: return f"{self.get_field_name()} < {value}"
    def lte(self, value) -> str: return f"{self.get_field_name()} <= {value}"
    def in_(self, values) -> str: return f"{self.get_field_name()} IN {values}"
    def not_in_(self, values) -> str: return f"{self.get_field_name()} NOT IN {values}"
    def is_null(self) -> str: return f"{self.get_field_name()} IS NULL"
    def is_not_null(self) -> str: return f"{self.get_field_name()} IS NOT NULL"