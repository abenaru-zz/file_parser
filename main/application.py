import numbers
import time
from typing import Tuple, Callable, Any, Union

from utils.requirements.abstract import Executable, Validatable
from utils.validation.invalidate import InvalidationHandler


class Main(Validatable, Executable):
    def __init__(self, precondition: bool) -> None:
        self.__precondition = self.__class__._validate(('precondition', precondition))

    def __call__(self, function_a: Callable, function_b: Callable, sleep_time_in_seconds: int = 0) -> Any:
        while True:
            try:
                function_a()
            except KeyboardInterrupt as err:
                pass
            finally:
                function_b()
            time.sleep(self.__class__._validate(('time', sleep_time_in_seconds)))

    @classmethod
    def _validate(cls, validation_target_info: Tuple[str, Union[int, bool]]) -> Union[int, bool]:
        validation_options = {
            'precondition': cls.__validate_precondition,
            'time': cls.__validate_time
        }
        return validation_options[validation_target_info[0]](validation_target_info[1])

    @staticmethod
    def __validate_precondition(precondition: bool) -> bool:
        return InvalidationHandler.invalidate_if_not_instance_of(bool, ('precondition', precondition))

    @staticmethod
    def __validate_time(time_in_seconds: numbers.Complex) -> numbers.Complex:
        return InvalidationHandler.invalidate_if_is_smaller_than(0, ('time', time_in_seconds))
