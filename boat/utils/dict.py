from typing import TypeVar

from boat.utils.field import Field


__all__ = ('FieldDict', 'FieldDictDecorator',)


Model = TypeVar('Model')


class FieldDict:
    def __init__(self, table_name: str = ''):
        self._table_name = table_name

    def __getitem__(self, item: str) -> Field:
        return Field(item, table_name=self._table_name)


class FieldDictDecorator(property):
    def __get__(self, instance, owner: Model) -> FieldDict:
        return FieldDict(table_name=owner.__table_name__)
