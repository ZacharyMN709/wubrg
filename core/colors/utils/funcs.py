from typing import AnyStr
from core.colors.utils.types import ColorString, ColorIdentityString, PentadIdentityString, \
    SplashIdentityString, ColorCombinationIdentityString

from core.colors.utils.types import COLOR_IDENTITIES, PENTAD_STRING

from core.colors.utils import types


_COLOR_TO_PENTAD: dict[ColorIdentityString, PentadIdentityString]
_COLOR_TO_PENTAD = {k: v for k, v in zip(COLOR_IDENTITIES, PENTAD_STRING)}

_PENTAD_TO_COLOR: dict[PentadIdentityString, ColorIdentityString]
_PENTAD_TO_COLOR = {v: k for k, v in _COLOR_TO_PENTAD.items()}


# region Color Conversions
def color_to_splash(main_color: ColorIdentityString) -> SplashIdentityString:
    """
    Converts a ColorIdentityString to a SplashIdentityString, mainly for type-checking.

    :param main_color: The ColorIdentityString to convert.
    :return: The SplashIdentityString.
    """
    val: AnyStr = main_color.lower()
    return val


def splash_to_color(splash_color: SplashIdentityString) -> ColorIdentityString:
    """
    Converts a SplashIdentityString to a ColorIdentityString, mainly for type-checking.

    :param splash_color: The SplashIdentityString to convert.
    :return: The ColorIdentityString.
    """
    val: AnyStr = splash_color.upper()
    return val


def color_to_pentad(main_color: ColorIdentityString) -> PentadIdentityString:
    """
    Converts a ColorIdentityString to a PentadIdentityString.

    :param main_color: The ColorIdentityString to convert.
    :return: The PentadIdentityString.
    """
    val: AnyStr = _COLOR_TO_PENTAD[main_color]
    return val


def pentad_to_color(pentad_color: PentadIdentityString) -> ColorIdentityString:
    """
    Converts a PentadIdentityString to a ColorIdentityString.

    :param pentad_color: The PentadIdentityString to convert.
    :return: The ColorIdentityString.
    """
    val: AnyStr = _PENTAD_TO_COLOR[pentad_color]
    return val


def parse_color_identity(val: str) -> ColorIdentityString:
    """
    Converts a string to a ColorIdentityString.

    Converts the string to uppercase, and then adds each character in 'WUBRG'
    to a list, if it existed in the uppercase string, then joins the list.
    NOTE: This does not specially handle aliases, will treat them as regular strings.

    Eg: ``'{12]{G}{G}' -> 'G'``,  ``'Boros' -> 'B'``

    :param val: The string to parse the ColorIdentityString from.
    :return: The ColorIdentityString.
    """
    s: set[ColorString] = set(val.upper())
    val: AnyStr = ''.join([c for c in custom_types.WUBRG if c in s])
    return val


def parse_splash_identity(val: str) -> SplashIdentityString:
    """
    Converts a string to a SplashIdentityString.

    Converts the string to ColorIdentityString (using ``parse_color_identity``),
    then returns it as lower case.

    Eg: ``'{12]{G}{G}' -> 'g'``,  ``'Boros' -> 'b'``

    :param val: The string to parse the SplashIdentityString from.
    :return: The SplashIdentityString.
    """
    val: AnyStr = parse_color_identity(val).lower()
    return val


def gen_color_combination_identity(
        main_color: ColorIdentityString,
        splash_color: SplashIdentityString
) -> ColorCombinationIdentityString:
    """
    Concatenates a ColorIdentityString and a SplashIdentityString into a ColorCombinationIdentityString.

    :param main_color: The ColorIdentityString to concatenate.
    :param splash_color: The SplashIdentityString to concatenate.
    :return: The ColorCombinationIdentityString, if the result is valid.
    :raises ValueError: If the result would not be a valid ColorCombinationIdentityString.
    """
    s: AnyStr = main_color + splash_color
    if s not in custom_types.COLOR_COMBINATION_IDENTITIES:
        raise ValueError(f"`main_color` and `splash_color` cannot overlap. ({main_color}, {splash_color})")
    return s


def split_color_combination_identity(
        combo_string: ColorCombinationIdentityString
) -> tuple[ColorIdentityString, SplashIdentityString]:
    """
    Splits a ColorCombinationIdentityString into a ColorIdentityString and SplashIdentityString.

    :param combo_string: The ColorCombinationIdentityString to split.
    :return: The ColorIdentityString and SplashIdentityString
    """
    s: set[ColorString] = set(combo_string)
    main_str: AnyStr = ''.join([c for c in custom_types.WUBRG if c in s])
    splash_str: AnyStr = ''.join([c for c in custom_types.WUBRG.lower() if c in s])
    return main_str, splash_str
# endregion Color Conversions
