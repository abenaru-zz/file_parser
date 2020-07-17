from typing import Tuple, Any, Iterable

from utils.validation.custom_errors import InvalidTypeError, NameLengthError, ObjectNotFoundError


class InvalidationHandler:
    @staticmethod
    def invalidate_if_has_length_smaller_than(required_length: int, content_info: Tuple[str, Any]) -> Any:
        if len(content_info[1]) < required_length:
            raise NameLengthError(f'Length for {content_info[0]} should be greater than {required_length}.')
        return content_info[1]

    @staticmethod
    def invalidate_if_not_instance_of(clazz, content_info: Tuple[str, Any]) -> Any:
        if not isinstance(content_info[1], clazz):
            raise InvalidTypeError(f'The provided {content_info[0]} is not an instance of {clazz}.')
        return content_info[1]

    @staticmethod
    def invalidate_if_not_in(iterable: Iterable, content_info: Tuple[str, Any]) -> Any:
        if content_info[1] not in iterable:
            raise ObjectNotFoundError(f'The provided {content_info[0]} is unregistered.')
        return content_info[1]
