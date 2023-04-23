from __future__ import annotations
from typing import Iterator

from core.utilities.extensions import ExtendedFlagEnum
from core.colors.utils.types import ColorIdentityString, ColorAliasString, PentadIdentityString
from core.colors.utils import types, funcs

########################################################################
# ColorIdentity
########################################################################
# region Index Mappings
_WUBRG_CI_INDEX_MAP: [int, int] = {
    0: 0,
    1: 1,
    2: 2,
    4: 3,
    8: 4,
    16: 5,
    3: 6,
    5: 7,
    9: 8,
    17: 9,
    6: 10,
    10: 11,
    18: 12,
    12: 13,
    20: 14,
    24: 15,
    7: 16,
    11: 17,
    19: 18,
    13: 19,
    21: 20,
    25: 21,
    14: 22,
    22: 23,
    26: 24,
    28: 25,
    15: 26,
    23: 27,
    27: 28,
    29: 29,
    30: 30,
    31: 31,
}

_PENTAD_CI_INDEX_PATCH: [int, int] = {
    3: 6,
    6: 7,
    12: 8,
    24: 9,
    17: 10,

    5: 11,
    20: 12,
    18: 13,
    10: 14,
    9: 15,

    11: 16,
    22: 17,
    13: 18,
    26: 19,
    21: 20,

    7: 21,
    14: 22,
    28: 23,
    25: 24,
    19: 25,
}
# endregion Index Mappings


class ColorIdentity(ExtendedFlagEnum):
    """
    Implements the concept of a color identity.

    The Flag enum allows for set-like operations, without having multiple
    instances of identical sets. Also, being a class, it can be extended to
    support additional information, like number of colours the identity contains.
    """
    # region Constructors / Factory Methods
    @classmethod
    def from_name(cls, name: ColorIdentityString | ColorAliasString) -> ColorIdentity:
        """
        Returns a ColorIdentity for the provided string.

        :param name: The ColorIdentityString or ColorAliasString representing the colour.
        :return: A ColorIdentity matching the string.
        :raises KeyError: If the value provided doesn't exist in ColorIdentity. (This should only happen if
        something not of type ColorIdentityString or ColorAliasString is provided as an argument.)
        """
        # If the name is the empty string, count that as colorless.
        if name == '' or name == 'Colorless':
            return ColorIdentity.C

        # ColorAlias should inherently exist in the member map.
        return cls[name]
    # endregion Constructors / Factory Methods

    # region Enumeration Flags
    # region Base Colour Identities
    C = 0

    W = 1
    U = 2
    B = 4
    R = 8
    G = 16

    WU = W | U
    WB = W | B
    WR = W | R
    WG = W | G
    UB = U | B
    UR = U | R
    UG = U | G
    BR = B | R
    BG = B | G
    RG = R | G

    WUB = W | U | B
    WUR = W | U | R
    WUG = W | U | G
    WBR = W | B | R
    WBG = W | B | G
    WRG = W | R | G
    UBR = U | B | R
    UBG = U | B | G
    URG = U | R | G
    BRG = B | R | G

    WUBR = W | U | B | R
    WUBG = W | U | B | G
    WURG = W | U | R | G
    WBRG = W | B | R | G
    UBRG = U | B | R | G

    WUBRG = W | U | B | R | G
    # endregion Base Colour Identities

    # region Colour Aliases
    # region One-Color Aliases
    White = W
    Blue = U
    Black = B
    Red = R
    Green = G

    MonoWhite = W
    MonoBlue = U
    MonoBlack = B
    MonoRed = R
    MonoGreen = G

    Ardenvale = W
    Vantress = U
    Locthwain = B
    Embereth = R
    Garenbrig = G

    Auriok = W
    Neurok = U
    Moriok = B
    Vulshok = R
    Sylvok = G
    # endregion One-Color Aliases

    # region Two-Color Aliases
    Azorius = WU
    Dimir = UB
    Rakdos = BR
    Gruul = RG
    Selesnya = WG

    Orzhov = WB
    Golgari = BG
    Simic = UG
    Izzet = UR
    Boros = WR

    Ojutai = WU
    Silumgar = UB
    Kolaghan = BR
    Atarka = RG
    Dromoka = WG

    Silverquill = WB
    Witherbloom = BG
    Quandrix = UG
    Prismari = UR
    Lorehold = WR
    # endregion Two-Color Aliases

    # region Three-Color Aliases
    Jeskai = WUR
    Sultai = UBG
    Mardu = WBR
    Temur = URG
    Abzan = WBG

    Raugrin = WUR
    Zagoth = UBG
    Savai = WBR
    Ketria = URG
    Indatha = WBG

    Numot = WUR
    Vorosh = UBG
    Oros = WBR
    Intet = URG
    Teneb = WBG

    Raka = WUR
    Ana = UBG
    Dega = WBR
    Ceta = URG
    Necra = WBG

    Esper = WUB
    Grixis = UBR
    Jund = BRG
    Naya = WRG
    Bant = WUG

    Obscura = WUB
    Maestros = UBR
    Riveteers = BRG
    Cabaretti = WRG
    Brokers = WUG
    # endregion Three-Color Aliases

    # region Four-Color Aliases
    Yore = WUBR
    Witch = WUBG
    Ink = WURG
    Dune = WBRG
    Glint = UBRG

    Artifice = WUBR
    Growth = WUBG
    Altruism = WURG
    Aggression = WBRG
    Chaos = UBRG

    NonG = WUBR
    NonR = WUBG
    NonB = WURG
    NonU = WBRG
    NonW = UBRG
    # endregion Four-Color Aliases

    # region Five-Color Aliases
    FiveColor = WUBRG
    All = WUBRG
    # endregion Five-Color Aliases
    # endregion Colour Aliases
    # endregion Enumeration Flags

    # region Class Functions
    @classmethod
    def get_color_combinations(cls, _min: int = 0, _max: int = 5) -> list[ColorIdentity]:
        """
        Gets a list of color identities which have a number of colours between the min and max bounds, inclusive.

        :param _min: The minimum number of colours a colour identity should contain.
        :param _max: The maximum number of colours a colour identity should contain.
        :return: The list of colour identities, in WUBRG order.
        """
        return [ci for ci in ColorIdentity if _min <= ci.color_count <= _max]

    @classmethod
    def colors(cls) -> list[ColorIdentity]:
        """
        Gets the ColorIdentity for each color of Magic: White, Blue, Black, Red, Green.

        :return: Returns a list of the 5 base colours.
        """
        return cls.get_color_combinations(1, 1)
    # endregion Class Functions

    # region Instance Functions / Properties
    # region Color Properties
    @property
    def color_count(self) -> int:
        """The number of colours in the ColorIdentity."""
        count = 0
        val = self.value
        while val != 0:
            count += int(val & 1)  # Adds one to the count if the last bit is a 1.
            val = val >> 1
        return count

    @property
    def aliases(self) -> list[ColorAliasString]:
        """
        Gets a list of ColorAliasString, which are aliases (or the base name) for the ColorIdentity.

        Eg: ``WU -> ['WU', 'Azorius', 'Ojutai']``
        """
        if self == ColorIdentity.C:
            return ['C', 'Colorless', '']
        return [k for k, v in self._member_map_.items() if v == self]

    @property
    def alias(self) -> ColorAliasString:
        """
        Gets a string, which is the common alias for the ColorIdentity.

        Eg: ``WU -> 'Azorius'``
        """
        return self.aliases[1]

    @property
    def wubrg_str(self) -> ColorIdentityString:
        """Return the ColorIdentityString for the ColorIdentity."""
        if self.name == 'C':
            return ''
        else:
            return self.name

    @property
    def pentad_str(self) -> PentadIdentityString:
        """Return the PentadString for the ColorIdentity."""
        return funcs.color_to_pentad(self.wubrg_str)
    # endregion Color Properties

    # region Index Properties
    @property
    def wubrg_idx(self) -> int:
        """Generates the sorting index for wubrg order."""
        return _WUBRG_CI_INDEX_MAP[self.value]

    @property
    def pentad_idx(self) -> int:
        """Generates the sorting index for pentad order."""
        if self.value in _PENTAD_CI_INDEX_PATCH:
            return _PENTAD_CI_INDEX_PATCH[self.value]
        else:
            return _WUBRG_CI_INDEX_MAP[self.value]

    @property
    def deck_idx(self) -> int:
        """Generates the sorting index for deck building order."""
        new_val = _WUBRG_CI_INDEX_MAP[self.value] - 1
        if new_val < 0:
            new_val += len(custom_types.COLOR_IDENTITIES)
        return new_val
    # endregion Index Properties

    # region Set-Like Properties
    @property
    def exact(self) -> list[ColorIdentity]:
        """
        Returns a list of ColorIdentity which exactly match the ColorIdentity.

        Eg: ``WU -> [WU]``
        """
        return [self]

    @property
    def subset(self) -> list[ColorIdentity]:
        """
        Returns a list of ColorIdentity which are a non-strict subset of ColorIdentity.

        Eg: ``WU -> [W, U, WU]``
        """
        return [ci for ci in ColorIdentity if ci <= self]

    @property
    def superset(self) -> list[ColorIdentity]:
        """
        Returns a list of ColorIdentity which are a non-strict superset of ColorIdentity.

        Eg: ``WU -> [WU, WUB, WUR, WUG... WUBRG]``
        """
        return [ci for ci in ColorIdentity if ci >= self]

    @property
    def adjacent(self) -> list[ColorIdentity]:
        """
        Returns a list of ColorIdentity which are no more than one colour different than ColorIdentity.

        Eg: ``WU -> [WU, U, W, WUB, WUR, WUG]``
        """
        return [self ^ ci for ci in self.get_color_combinations(0, 1)]

    @property
    def shares(self) -> list[ColorIdentity]:
        """
        Returns a list of ColorIdentity which shares any color with ColorIdentity.

        Eg: ``WU -> [W, U, WU, WB... UB... WUBRG]``
        """
        return [ci for ci in ColorIdentity if (self & ci)]
    # endregion Set-Like Properties

    # region Comparator Functions
    def __eq__(self, other: ColorIdentity) -> bool:
        return self.value == other.value

    def __ne__(self, other: ColorIdentity) -> bool:
        return not self.__eq__(other)

    def __ge__(self, other: ColorIdentity) -> bool:
        return other in self

    def __le__(self, other: ColorIdentity) -> bool:
        return self in other

    def __gt__(self, other: ColorIdentity) -> bool:
        return (not self.__eq__(other)) and self.__ge__(other)

    def __lt__(self, other: ColorIdentity) -> bool:
        return (not self.__eq__(other)) and self.__le__(other)
    # endregion Comparator Functions

    def __iter__(self) -> Iterator[ColorIdentity]:
        """Returns an Iterator, with a ColorIdentity for each color in ColorIdentity."""
        return iter(ColorIdentity.from_name(c) for c in self.name)

    def __str__(self) -> str:
        """Returns the name of the ColorIdentity."""
        return self.name

    def __hash__(self):
        return self.value
    # endregion Instance Functions / Properties
