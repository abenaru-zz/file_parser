from abc import ABC, abstractmethod
from typing import Tuple, Any, Callable


class Validatable(ABC):
    @classmethod
    @abstractmethod
    def _validate(cls, validation_target_info: Tuple[str, Any]) -> Any:
        pass


class Executable(ABC):
    @abstractmethod
    def __call__(self, *args, **kwargs) -> Any:
        pass
