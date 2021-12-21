from boat.utils.dict import FieldDictDecorator


__all__ = ('Model',)


class Model:
    __table_name__: str

    @FieldDictDecorator
    def fields(cls):
        pass
