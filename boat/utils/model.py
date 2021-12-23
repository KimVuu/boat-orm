from boat.utils.field import Field


__all__ = ('FieldDict', 'FieldDictDecorator', 'Model',)


class FieldDict:
    def __init__(self, table_name: str = ''):
        self._table_name = table_name

    def __getitem__(self, item: str) -> Field:
        return Field(item, table_name=self._table_name)


class FieldDictDecorator(property):
    def __get__(self, *args, **kwargs):
        owner: "Model" = args[1]
        return FieldDict(owner.__table_name__)


class Model:
    __table_name__: str

    fields: FieldDict = FieldDictDecorator()
