import time
from typing import Tuple, Callable, Any

from utils.requirements.abstract import Executable, Validatable
from utils.validation.invalidate import InvalidationHandler


class Main(Validatable, Executable):
    def __init__(self, precondition: bool) -> None:
        self.__precondition = InvalidationHandler.invalidate_if_not_instance_of(bool, ('precondition', precondition))

    def __call__(self, function: Callable, sleep_time_in_seconds: int = 0) -> Any:
        while True:
            try:
                function()
            except KeyboardInterrupt as err:
                exit()
            time.sleep(sleep_time_in_seconds)

    @classmethod
    def _validate(cls, validation_target_info: Tuple[str, bool]) -> bool:
        validation_options = {
            'precondition': cls.__validate_precondition,
        }
        return validation_options[validation_target_info[0]](validation_target_info[1])

    @staticmethod
    def __validate_precondition(precondition: bool) -> bool:
        return InvalidationHandler.invalidate_if_not_instance_of(bool, ('precondition', precondition))
