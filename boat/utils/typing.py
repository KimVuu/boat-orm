from abc import abstractmethod
from typing import Any, List, Dict

from boat.utils import abc


class SqlValue(abc.SqlValue):
    format: str

    @abstractmethod
    def get_value(self) -> Any: pass

    @abstractmethod
    def get_kwargs(self) -> Dict[str, Any]: pass

    @abstractmethod
    def get_format(self) -> str: pass

    @abstractmethod
    def get_sql(self) -> str: pass

    @abstractmethod
    def get_bindings(self) -> List[Any]: pass
