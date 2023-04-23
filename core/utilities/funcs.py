from typing import Union, Optional, TypeVar
from itertools import chain
from collections import Counter
from os import path
import json

from core.utilities.auto_logging import logging

ENCODING = 'utf-8'

T = TypeVar('T')
T1 = TypeVar('T1')
T2 = TypeVar('T2')


def flatten_lists(lst: list[list[T]]) -> list[T]:
    """Converts a list of lists into a single list"""
    return [item for sublist in lst for item in sublist]


def lists_equal(l_lst: list[T], r_lst: list[T]) -> bool:
    """Checks if two lists are equal, identical elements in identical order."""
    # If the list aren't equal length, skip any further checks.
    if len(l_lst) != len(r_lst):
        return False

    # Compare each element, return False if they don't match. If we don't find mismatches, return True.
    for i in range(0, len(l_lst)):
        if l_lst[i] != r_lst[i]:
            return False
    return True


# Taken from: https://stackoverflow.com/questions/3428536/how-do-i-subtract-one-list-from-another/57827145#57827145
def subtract_lists(l_lst: list[T], r_lst: list[T], right_to_left=False) -> list[T]:
    """Returns a copy of the left list, minus any elements in the right list."""
    out = []
    remaining = Counter(r_lst)

    # Get the correct iterable based on right_to_left.
    if right_to_left:
        elements = reversed(l_lst)
    else:
        elements = l_lst

    # Create the list to return, using the Counter to track what's removed.
    for val in elements:
        if remaining[val]:
            remaining[val] -= 1
        else:
            out.append(val)

    # Revers the list if necessary, to retain the original order, then return the list.
    if right_to_left:
        out.reverse()
    return out


def weave_lists(l1: list[T], l2: list[T]) -> list[T]:
    """Interweaves elements of two equal-length lists into one."""
    if len(l1) != len(l2):
        raise ValueError("List length must be equal!")
    return list(chain.from_iterable(zip(l1, l2)))


def invert_dict(d: dict[T1, T2]) -> dict[T2, T1]:
    """Creates a new dictionary with the keys and values swapped."""
    return {v: k for k, v in d.items()}


def validate_json(json_str: str) -> bool:
    """
    Checks to see if a provided string is valid json.

    :param json_str: The string to check.
    :return: Whether the string is valid json.
    """
    try:
        json.loads(json_str)
    except ValueError:
        return False
    return True


def load_json_file(folder: str, filename: str) -> Union[dict, list[dict], None]:
    """
    Loads and returns the data from a json file.

    :param folder: The folder the json file is in.
    :param filename: The name of the json file (including filetype).
    :return: An object containing the json data.
    """
    filepath = path.join(folder, filename)

    try:
        with open(filepath, 'r', encoding=ENCODING) as f:
            json_str = f.read()
            f.close()
            logging.verbose(f'File {filename} read successfully.')
            return json.loads(json_str)
    except Exception as ex:
        logging.error(f'Error reading json file {filename}')
        logging.error(ex)
        return None


def save_json_file(folder: str, filename: str, data: [dict, list[dict]], indent: Optional[int] = 4) -> bool:
    """
    Saves provided data into the specified json file.

    :param folder: The folder the json file is in.
    :param filename: The name of the json file (including filetype).
    :param data: The object to be saved as json.
    :param indent: The indenting to use for the json.
    :return: Whether the save operation was successful.
    """
    filepath = path.join(folder, filename)

    try:
        with open(filepath, 'w', encoding=ENCODING) as f:
            f.write(json.dumps(data, indent=indent))
            f.close()
        logging.verbose(f'File {filename} written to.')
        return True
    except Exception as ex:
        logging.error(f'Error writing to json file {filename}')
        logging.error(ex)
        return False


def reformat_json_file(folder: str, filename: str, indent: Optional[int] = 4) -> None:
    """
    Re-writes the json file in question, if it can be parsed, with the provided indents.

    :param folder: The folder the json file is in.
    :param filename: The name of the json file (including filetype).
    :param indent: The indenting to use for the json.
    """
    data = load_json_file(folder, filename)
    if data:
        save_json_file(folder, filename, data, indent=indent)


def isolate_string(text: str, isolate_from: str = None, isolate_to: str = None):
    """
    Isolates a portion of a string based on the first found instances of a from and to string.

    :param text: The text to isolate a string from.
    :param isolate_from: The string to start isolating from.
    :param isolate_to: The string to isolate up to.
    :return: The isolated string.
    """
    if isolate_from:
        start_idx = text.index(isolate_from) + len(isolate_from)
    else:
        start_idx = None

    if isolate_to:
        end_idx = text.index(isolate_to, start_idx)
    else:
        end_idx = None

    truncated_text = text[start_idx:end_idx].strip()
    return truncated_text


def format_seconds(seconds: float) -> tuple[float, str]:
    """
    Converts an amount of second to a more natural time value and unit (up to days).

    :param seconds: The time taken, in seconds.
    :return: The float value of time, and the unit of time.

    Eg: ``140 -> 2.34, 'minute'``
    """
    time_units = ['millisecond', 'second', 'minute', 'hour', 'day']
    time_divisors = [1000, 60, 60, 24]

    idx = 0
    time_elapsed = seconds * 1000
    while idx < len(time_divisors) and time_elapsed >= time_divisors[idx]:
        time_elapsed = time_elapsed / time_divisors[idx]
        idx += 1

    return time_elapsed, time_units[idx]
