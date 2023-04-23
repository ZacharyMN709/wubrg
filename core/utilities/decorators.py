from typing import Callable, Hashable, Any
from functools import wraps
import logging
from time import sleep, time
from unittest import TestLoader

from core.utilities.funcs import format_seconds


# Adapted/Taken from https://towardsdatascience.com/python-decorators-for-data-science-6913f717669a
def retry(max_tries: int, fail_delay: float):
    """
    A decorator which attempts to rerun a function if it fails, with a delay between each try.

    :param max_tries: The max number of times the function should be run.
    :param fail_delay: The delay (in seconds) between runs.
    :return: Returns the parameterized decorator.
    """
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            tries = 0
            while tries < max_tries:
                try:
                    return func(*args, **kwargs)
                except Exception as e:
                    tries += 1
                    if tries == max_tries:
                        raise e
                    sleep(fail_delay)
        return wrapper
    return decorator


# Adapted/Taken from https://towardsdatascience.com/python-decorators-for-data-science-6913f717669a
def memoize(cache_obj: dict[Hashable, Any] = None):
    """
    A decorator which automatically caches the results of a function call.

    :param cache_obj: The cache to place results into.
    :return: Returns the parameterized decorator.
    """
    if cache_obj is None:
        cache_obj = dict()

    def decorator(func: Callable):
        @wraps(func)
        def wrapper(*args):
            if args not in cache_obj:
                result = func(*args)
                cache_obj[args] = result
            return cache_obj[args]
        return wrapper
    return decorator


# Adapted/Taken from https://towardsdatascience.com/python-decorators-for-data-science-6913f717669a
def time_execution(log_func: Callable[[str], None] = print):
    """
    A decorator which times the execution of a function.

    :param log_func: The function which handles the logging messages. Default is `print`.
    :return: Returns the parameterized decorator.
    """
    def decorator(func: Callable):
        @wraps(func)
        def wrapper(*args, **kwargs):
            start_time = time()
            result = func(*args, **kwargs)
            end_time = time()
            time_val, time_unit = format_seconds(end_time - start_time)
            log_func(f"Function {func.__name__} took {round(time_val, 3)} {time_unit}s.")
            return result
        return wrapper
    return decorator


# Adapted/Taken from https://towardsdatascience.com/python-decorators-for-data-science-6913f717669a
def log_execution(log_func: Callable[[str], None] = logging.debug):
    """
    A decorator which logs the start and end of a function call.

    :param log_func: The function which handles the logging messages. Default is `logging.debug`.
    :return: Returns the parameterized decorator.
    """
    def decorator(func: Callable):
        @wraps(func)
        def wrapper(*args, **kwargs):
            log_func(f"Executing {func.__name__}...")
            result = func(*args, **kwargs)
            log_func(f"Finished executing {func.__name__}...")
            return result
        return wrapper
    return decorator


# Adapted/Taken from https://towardsdatascience.com/python-decorators-for-data-science-6913f717669a
def notify_on_failure(notifier: Callable[[Exception, str], None]):
    """
    A decorator which sends a notification if the provided function fails.

    :param notifier: A function which takes in the exception and function name, and sends an notification.
    :return: Returns the parameterized decorator.
    """
    def decorator(func: Callable):
        @wraps(func)
        def wrapper(*args, **kwargs):
            try:
                return func(*args, **kwargs)
            except Exception as e:
                notifier(e, func.__name__)
                raise e
        return wrapper
    return decorator


# Adapted from: https://codereview.stackexchange.com/questions/122532/controlling-the-order-of-unittest-testcases
def custom_order_tests(loader: TestLoader, ordering_dict: dict = None):
    """
    Returns a parameterizable decorator which is to be placed before test functions.

    The returned function takes in an optional int, which specifies the index for
    the test. If no index is provided, the test is assigned the maximum value among
    indexes plus one, placing it as the last test to be run. Attempting to assign a
    an index which is already taken will raise an AssertionError.

    The returned function, itself, returns the decorator that's used. If tests only
    need to be ran in the order they're written in the file, that decorator can
    be extracted and used, instead of using the parameterized version.

    :param loader: The TestLoader to set the ordering for.
    :param ordering_dict: The dictionary to contain the ordering. If not provided, will be automatically created.
    :return: A parameterizable decorator to be placed before a test function.

    Example Usage::

        ordered = decorators.custom_order_tests(unittest.defaultTestLoader)
        auto_ordered = ordered()  # Getting the underlying decorator.

        @ordered(-1)  # The parameterizable decorator, with value.
        def test_true(self):
            self.assertTrue(True)

        @auto_ordered  # The 'unpacked' decorator.
        def test_false(self):
            self.assertFalse(False)

        @ordered()  # The parameterized decorator using the default.
        def test_equal(self):
            self.assertEqual(True, False)
    """
    if ordering_dict is None:
        ordering_dict = dict()

    def compare(a, b):
        """Handles index comparisons, placing un-indexed functions last."""
        try:
            return ordering_dict[a] - ordering_dict[b]
        except KeyError:  # Handles if undecorated tests are run.
            if a in ordering_dict:
                return -1
            else:
                return 1

    def custom_orderer(idx: int = None):
        """
        The parameterizable decorator.

        :param idx: The index to assign the test.
        :return: The decorator to apply.
        :raises AssertionError: Raised if the ``idx`` is already in use.
        """
        if idx is None:
            if ordering_dict.values():
                idx = max(ordering_dict.values()) + 1
            else:
                idx = 1
        else:
            assert idx not in ordering_dict.values(), f"Index {idx} already taken."

        def apply_order(func):
            """The decorator which applies an order to a test."""
            logging.debug(f"Adding {func.__name__}: {idx}")
            ordering_dict[func.__name__] = idx

            @wraps(func)
            def wrapper(*args, **kwargs):
                """Logs the execution of the test."""
                logging.debug(f"Running test {idx}: {func.__name__}...")
                result = func(*args, **kwargs)
                return result

            return wrapper

        return apply_order

    loader.sortTestMethodsUsing = compare
    return custom_orderer
