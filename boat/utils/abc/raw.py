from abc import ABC, abstractmethod


class SqlValue(ABC):
    @abstractmethod
    def get_value(self):
        pass

    @abstractmethod
    def get_kwargs(self):
        pass

    @abstractmethod
    def get_format(self):
        pass

    @abstractmethod
    def get_sql(self):
        pass

    @abstractmethod
    def get_bindings(self):
        pass
