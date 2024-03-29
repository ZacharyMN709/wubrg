from typing import Optional, NoReturn
from enum import IntEnum, unique
import logging


@unique
class LogLvl(IntEnum):
    """Logging levels, based off of ``logging``'s "enum"."""
    CRITICAL = 50
    ERROR = 40
    WARNING = 30
    SPARSE = 25
    INFO = 20
    VERBOSE = 15
    DEBUG = 10
    NOTSET = 0


# Taken from: https://stackoverflow.com/a/35804945/1691778
def add_logging_level(level_name: str, level_num: int, method_name: str = None) -> Optional[NoReturn]:
    """
    Comprehensively adds a new logging level to the ``logging`` module and the
    currently configured logging class.

    ``level_name`` becomes an attribute of the ``logging`` module with the value
    ``level_num``. ``method_name`` becomes a convenience method for both `logging`
    itself and the class returned by ``logging.getLoggerClass()`` (usually just
    ``logging.Logger``). If ``method_name`` is not specified, ``level_name.lower()``
    is used.

    To avoid accidental clobbering of existing attributes, this method will
    raise an ``AttributeError`` if the level name is already an attribute of the
    ``logging`` module or if the method name is already present.

    Example::

        addLoggingLevel('TRACE', logging.DEBUG - 5)
        logging.getLogger(__name__).setLevel("TRACE")
        logging.getLogger(__name__).trace('that worked')
        logging.trace('so did this')
        logging.TRACE  # 5
    """
    if not method_name:
        method_name = level_name.lower()

    if hasattr(logging, level_name):
        raise AttributeError(f'{level_name} already defined in logging module')
    if hasattr(logging, method_name):
        raise AttributeError(f'{method_name} already defined in logging module')
    if hasattr(logging.getLoggerClass(), method_name):
        raise AttributeError(f'{method_name} already defined in logger class')

    def log_for_level(self, message, *args, **kwargs):
        if self.isEnabledFor(level_num):
            self._log(level_num, message, args, **kwargs)

    def log_to_root(message, *args, **kwargs):
        logging.log(level_num, message, *args, **kwargs)

    logging.addLevelName(level_num, level_name)
    setattr(logging, level_name, level_num)
    setattr(logging.getLoggerClass(), method_name, log_for_level)
    setattr(logging, method_name, log_to_root)


def add_custom_levels() -> None:
    """Adds any missing log levels from LogLvl as values and functions to the logging module."""
    for lvl in LogLvl:
        try:
            add_logging_level(lvl.name.upper(), lvl, lvl.name.lower())
        except AttributeError:
            pass


def set_log_level(lvl: LogLvl, filename: Optional[str] = None, filemode: Optional[str] = 'a') -> None:
    """
    Sets the log level, and formats the logging messages and timestamps.

    Can be optionally provided with a filename and filemode to output the logging to
    a file.

    The format of the logging messages will look similar to::

    [2023/03/19 04:20:48] SPARSE  : "Message!"

    :param lvl: The level to log at.
    :param filename: The filename to output the log to. Uses ``stdout`` if None.
    :param filemode: The filemode to use with the file. Default is 'a', for append.
    """
    # noinspection SpellCheckingInspection
    fmt = '[%(asctime)s] %(levelname)-8s: %(message)s'
    date_format = '%Y/%m/%d %H:%M:%S'
    logging.basicConfig(level=lvl, filename=filename, filemode=filemode, format=fmt, datefmt=date_format, force=True)


def auto_log(lvl: LogLvl = LogLvl.SPARSE) -> None:
    """
    Adds the custom levels to the logging, and sets the log level and style.

    The format of the logging messages uses a predefined default, which
    looks similar to::

    [2023/03/19 04:20:48] SPARSE  : "Message!"

    :param lvl: The log level to use.
    """
    add_custom_levels()
    set_log_level(lvl)


# When this module is loaded, automatically add in the custom levels of logging.
add_custom_levels()
