from __future__ import annotations
from typing import Iterator, Optional, cast
from enum import Flag

from core.colors.color_typing import ColorIdentityString, ColorAliasString

# region Index Mappings
WUBRG_CI_INDEX_MAP: [int, int] = {
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

PENTAD_CI_INDEX_PATCH: [int, int] = {
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


class ColorIdentity(Flag):
    color_count: int
    wubrg_idx: int
    pentad_idx: int
    deck_idx: int

    # region Constructors / Factory Methods
    def __init__(self, value: int):
        # region Index Generators
        def get_color_count(val: int) -> int:
            """Generates the number of colours in the ColorIdentity"""
            count = 0
            while val != 0:
                count += int(val & 1)  # Adds one to the count if the last bit is a 1.
                val = val >> 1
            return count

        def gen_wubrg_order_idx(val: int) -> int:
            """Generates the sorting index for wubrg order"""
            return WUBRG_CI_INDEX_MAP[val]

        def gen_pentad_order_idx(val: int) -> int:
            """Generates the sorting index for pentad order"""
            if val in PENTAD_CI_INDEX_PATCH:
                return PENTAD_CI_INDEX_PATCH[val]
            else:
                return WUBRG_CI_INDEX_MAP[val]

        def gen_deck_order_idx(val: int) -> int:
            """Generates the sorting index for deck building order"""
            new_val = WUBRG_CI_INDEX_MAP[val] - 1
            if new_val < 0:
                new_val = 31
            return new_val
        # endregion Index Generators

        self.color_count = get_color_count(value)
        self.wubrg_idx = gen_wubrg_order_idx(value)
        self.pentad_idx = gen_pentad_order_idx(value)
        self.deck_idx = gen_deck_order_idx(value)

    @classmethod
    def by_name(cls, name: ColorIdentityString | ColorAliasString) -> ColorIdentity:
        """
        Returns a color identity for the provided ColorIdentityString or ColorAlias string.
        :param name: The ColorIdentityString or ColorAliasString representing the colour.
        :return: A ColorIdentity matching the string.
        """
        # If the name is the empty string, count that as colorless.
        if name == '':
            return ColorIdentity.C

        # ColorAlias should inherently exist in the member map.
        return cls._member_map_[name]

    @classmethod
    def get(cls, name: str) -> Optional[ColorIdentity]:
        """
        Attempts to return a color identity for the provided string.
        :param name: The name of the colour or color alias.
        :return: A ColorIdentity matching the string, or None if the string cannot be matched.
        """

        # Return any guaranteed checks, if they're applicable.
        if isinstance(name, ColorIdentityString) or isinstance(name, ColorAliasString):
            return cls.by_name(cast(ColorIdentityString | ColorAliasString, name))

        # TODO: Consider adding some sort of color or cost parsing functionality to this.

        # As a last-resort, iterate through the keys and values of the
        #  member_map, using a case-insensitive matching.
        name = name.upper()
        for k, v in cls._member_map_.items():
            if k.upper() == name:
                return v

        return None
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
        Gets the base colors of Magic: White, Blue, Black, Red, Green.
        :return: Return a list of the 5 base colours.
        """
        return cls.get_color_combinations(1, 1)
    # endregion Class Functions

    # region Instance Functions / Properties
    # region Set-Like Properties
    @property
    def exact(self) -> list[ColorIdentity]:
        """Returns a list of ColorIdentity which exactly match the ColorIdentity"""
        return [self]

    @property
    def subset(self) -> list[ColorIdentity]:
        """Returns a list of ColorIdentity which are a non-strict subset of ColorIdentity"""
        return [ci for ci in ColorIdentity if ci in self]

    @property
    def superset(self) -> list[ColorIdentity]:
        """Returns a list of ColorIdentity which are a non-strict superset of ColorIdentity"""
        return [ci for ci in ColorIdentity if self in ci]

    @property
    def adjacent(self) -> list[ColorIdentity]:
        """Returns a list of ColorIdentity which are no more than one colour different than ColorIdentity"""
        return [self ^ ci for ci in self.get_color_combinations(0, 1)]

    @property
    def shares(self) -> list[ColorIdentity]:
        """Returns a list of ColorIdentity which shares any color with ColorIdentity"""
        return [ci for ci in ColorIdentity if (self & ci)]
    # endregion Set-Like Properties

    @property
    def aliases(self) -> list[ColorAliasString]:
        """Gets a list of strings, which are aliases or base names for the ColorIdentity"""
        if self == ColorIdentity.C:
            return ['C', '']
        return [k for k, v in self._member_map_.items() if v == self]

    def __iter__(self) -> Iterator[ColorIdentity]:
        """Gets an iterable of the colors contained in the color identity."""
        return iter(ColorIdentity.by_name(c) for c in self.name)

    def __str__(self) -> ColorIdentityString:
        """Return the ColorIdentityString of the ColorIdentity."""
        if self.name == 'C':
            return ''
        else:
            return self.name
    # endregion Instance Functions / Properties
