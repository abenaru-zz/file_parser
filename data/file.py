from typing import Any, Tuple, Callable

from utils.constants import ACCESS_MODES
from utils.requirements.abstract import Validatable, Executable
from utils.validation.invalidate import InvalidationHandler


class FileHandler(Validatable, Executable):
    def __init__(self, path: str, mode: str = 'read') -> None:
        self.__path = self.__class__._validate(('file', path))
        self.__mode = self.__class__._validate(('access mode', mode))

    @property
    def path(self) -> str:
        return self.__path

    @path.setter
    def path(self, path: str) -> None:
        self.__path = self.__class__._validate(('file', path))

    @property
    def mode(self) -> str:
        return self.__mode

    @mode.setter
    def mode(self, mode: str = 'read') -> None:
        self.__mode = self.__class__._validate(('access mode', mode))

    def __call__(self, function: Callable) -> Any:
        with open(self.path, ACCESS_MODES[self.mode]) as file:
            return function(file)

    @classmethod
    def _validate(cls, validation_target_info: Tuple[str, str]) -> str:
        validation_options = {
            'access mode': cls.__validate_mode,
            'file': cls.__validate_path
        }
        return validation_options[validation_target_info[0]](validation_target_info[1])

    @staticmethod
    def __validate_path(path: str) -> str:
        return InvalidationHandler.invalidate_if_has_length_smaller_than(1, ('file name', path))

    @staticmethod
    def __validate_mode(mode: str) -> str:
        return InvalidationHandler.invalidate_if_not_in(ACCESS_MODES, ('access mode', mode))
