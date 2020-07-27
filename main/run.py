import re
from io import TextIOWrapper
from typing import List, Tuple, Callable

from data.file import FileHandler
from main.application import Main
from utils.system.logging import SystemLoggingHandler


def get_debug_logs(file: TextIOWrapper) -> List[Tuple[str, str]]:
    pattern = '(.*) - (.*) - (.*) - (.*) - (.*) - (.*) - (.*)'

    return [
        (re.match(pattern, debug_log).group(6), re.match(pattern, debug_log).group(7))
        for debug_log in file if re.match(pattern, debug_log)
    ]


def write_to_file(debug_logs: List[Tuple[str, str]]) -> Callable:

    def write_to_file_internal(file: TextIOWrapper) -> None:
        cache = []
        for method, clazz in debug_logs:
            if method in cache:
                continue
            file.write(f'{clazz}.{method}\n')
            cache.append(method)

    return write_to_file_internal


def main() -> None:
    logger = SystemLoggingHandler('green', 'System')
    logger(print, 'Starting Simbiose Debug Log parser...')

    original_file_path = logger(input, 'Insert the path of the file to be parsed')
    new_file_path = logger(input, f'Insert the path of the file to be generated from "{original_file_path}"')

    logger(print, f'Instantiating the original file: "{original_file_path}"...')
    original_file = FileHandler(original_file_path)

    logger(print, f'Instantiating a new file: "{new_file_path}"...')
    new_file = FileHandler(new_file_path, 'write')

    logger(print, f'Fetching debug logs in the original file: "{original_file_path}"...')
    debug_logs_found = original_file(get_debug_logs)

    logger(print, f'Writing debug logs to a new file: "{new_file_path}"...')
    new_file(write_to_file(debug_logs_found))

    logger(print, 'Done!')


def terminate() -> None:
    logger = SystemLoggingHandler('red', 'System')
    answer = logger(input, 'Do you wish to terminate the application? (Y/N)').lower().strip()

    if answer == 'y':
        exit()
    elif answer == 'n':
        pass
    else:
        raise AssertionError(f'Invalid answer for a yes-or-no question: "{answer}".')


APPLICATION = Main(__name__ == '__main__')
APPLICATION(main, terminate, 5)
