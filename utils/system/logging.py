from typing import Tuple, Union, Callable, Any

from utils.constants import COLORS
from utils.requirements.abstract import Executable, Validatable
from utils.validation.invalidate import InvalidationHandler


class SystemLoggingHandler(Validatable, Executable):

    __DEFAULT_AUTHOR = 'SYSTEM'
    __DEFAULT_COLOR = 'reset'

    def __init__(self, color: str, author: Union[str, None] = None) -> None:
        self.__color = self.__class__._validate(('color', color))
        self.__author = self.__class__._validate(('author', author)) if author else self.__class__.get_default_author()

    @property
    def color(self) -> str:
        return self.__color

    @color.setter
    def color(self, name: str) -> None:
        self.__color = self.__class__._validate(('color', name))

    @property
    def author(self) -> str:
        return self.__author

    @author.setter
    def author(self, name: Union[str, None]) -> None:
        self.__author = self.__class__._validate(('author', name)) if name else self.__class__.__DEFAULT_COLOR

    def __call__(self, action: Callable, message: str) -> Union[Any, None]:
        actions = {
            input: self.__class__.__input
        }

        message = '{0}[{1}{2}{0}] {3}'.format(
            COLORS[self.__class__.__DEFAULT_COLOR],
            COLORS[self.color],
            self.author,
            InvalidationHandler.invalidate_if_has_length_smaller_than(1, ('message', message))
        )

        return actions.get(action, action)(message)

    @classmethod
    def get_default_author(cls):
        return cls.__DEFAULT_AUTHOR

    @classmethod
    def _validate(cls, validation_target_info: Tuple[str, str]) -> str:
        validation_options = {
            'author': cls.__validate_author,
            'color': cls.__validate_color
        }
        return validation_options[validation_target_info[0]](validation_target_info[1])

    @staticmethod
    def __input(message):
        return input(f'{message} -> ')

    @staticmethod
    def __validate_color(name: str) -> str:
        return InvalidationHandler.invalidate_if_not_in(COLORS, ('color', name))

    @staticmethod
    def __validate_author(name: str) -> str:
        return InvalidationHandler.invalidate_if_has_length_smaller_than(1, ('author', name))
