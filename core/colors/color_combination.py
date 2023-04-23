from __future__ import annotations
from typing import Iterator, AnyStr

from core.utilities.extensions import ExtendedFlagEnum
from core.colors.utils.types import ColorIdentityString, SplashIdentityString, ColorCombinationIdentityString
from core.colors.color_identity import ColorIdentity
from core.colors.utils import funcs, types


########################################################################
# ColorCombination
########################################################################
class ColorCombination(ExtendedFlagEnum):
    """
    Implements the concept of a color identity, with a splash.

    This is designed to support the idea of a splash.
    This objects doesn't prescribe *what* a splash is, but does
    provide some support to identify if a colour is splashing itself
    (eg. An Izzet deck splashing blue). The splashes are considered
    invalid, but raise no errors, as that would interfere with some logic.

    Bit-wise operations do not prevent creating an "invalid" ColorCombination
    (as doing something like inverting a flag is useful), so care should be
    taken when manipulating the objects. When in doubt, the ``is_valid``
    property can be checked to see if the ColorCombination is in a valid state.

    *Invalid ColorCombinations will NOT have name values.*
    """
    # region Enumeration Flags
    # region Base Flags
    C = 0

    # These are defined below, to naturally preserve WUBRG order.
    # W = 1
    # U = 2
    # B = 4
    # R = 8
    # G = 16

    w = 32
    u = 64
    b = 128
    r = 256
    g = 512
    # endregion Base Flags

    # region Colorless
    wu = w | u
    wb = w | b
    wr = w | r
    wg = w | g
    ub = u | b
    ur = u | r
    ug = u | g
    br = b | r
    bg = b | g
    rg = r | g
    wub = w | u | b
    wur = w | u | r
    wug = w | u | g
    wbr = w | b | r
    wbg = w | b | g
    wrg = w | r | g
    ubr = u | b | r
    ubg = u | b | g
    urg = u | r | g
    brg = b | r | g
    wubr = w | u | b | r
    wubg = w | u | b | g
    wurg = w | u | r | g
    wbrg = w | b | r | g
    ubrg = u | b | r | g
    wubrg = w | u | b | r | g
    # endregion Colorless

    # region One Colour
    # region W
    W = 1
    Wu = W | u
    Wb = W | b
    Wr = W | r
    Wg = W | g
    Wub = W | u | b
    Wur = W | u | r
    Wug = W | u | g
    Wbr = W | b | r
    Wbg = W | b | g
    Wrg = W | r | g
    Wubr = W | u | b | r
    Wubg = W | u | b | g
    Wurg = W | u | r | g
    Wbrg = W | b | r | g
    Wubrg = W | u | b | r | g
    # endregion W

    # region U
    U = 2
    Uw = U | w
    Ub = U | b
    Ur = U | r
    Ug = U | g
    Uwb = U | w | b
    Uwr = U | w | r
    Uwg = U | w | g
    Ubr = U | b | r
    Ubg = U | b | g
    Urg = U | r | g
    Uwbr = U | w | b | r
    Uwbg = U | w | b | g
    Uwrg = U | w | r | g
    Ubrg = U | b | r | g
    Uwbrg = U | w | b | r | g
    # endregion U

    # region B
    B = 4
    Bw = B | w
    Bu = B | u
    Br = B | r
    Bg = B | g
    Bwu = B | w | u
    Bwr = B | w | r
    Bwg = B | w | g
    Bur = B | u | r
    Bug = B | u | g
    Brg = B | r | g
    Bwur = B | w | u | r
    Bwug = B | w | u | g
    Bwrg = B | w | r | g
    Burg = B | u | r | g
    Bwurg = B | w | u | r | g
    # endregion B

    # region R
    R = 8
    Rw = R | w
    Ru = R | u
    Rb = R | b
    Rg = R | g
    Rwu = R | w | u
    Rwb = R | w | b
    Rwg = R | w | g
    Rub = R | u | b
    Rug = R | u | g
    Rbg = R | b | g
    Rwub = R | w | u | b
    Rwug = R | w | u | g
    Rwbg = R | w | b | g
    Rubg = R | u | b | g
    Rwubg = R | w | u | b | g
    # endregion R

    # region G
    G = 16
    Gw = G | w
    Gu = G | u
    Gb = G | b
    Gr = G | r
    Gwu = G | w | u
    Gwb = G | w | b
    Gwr = G | w | r
    Gub = G | u | b
    Gur = G | u | r
    Gbr = G | b | r
    Gwub = G | w | u | b
    Gwur = G | w | u | r
    Gwbr = G | w | b | r
    Gubr = G | u | b | r
    Gwubr = G | w | u | b | r
    # endregion G
    # endregion One Colour

    # region Two Colour
    # region WU
    WU = W | U
    WUb = W | U | b
    WUr = W | U | r
    WUg = W | U | g
    WUbr = W | U | b | r
    WUbg = W | U | b | g
    WUrg = W | U | r | g
    WUbrg = W | U | b | r | g
    # endregion WU

    # region WB
    WB = W | B
    WBu = W | B | u
    WBr = W | B | r
    WBg = W | B | g
    WBur = W | B | u | r
    WBug = W | B | u | g
    WBrg = W | B | r | g
    WBurg = W | B | u | r | g
    # endregion WB

    # region WR
    WR = W | R
    WRu = W | R | u
    WRb = W | R | b
    WRg = W | R | g
    WRub = W | R | u | b
    WRug = W | R | u | g
    WRbg = W | R | b | g
    WRubg = W | R | u | b | g
    # endregion WR

    # region WG
    WG = W | G
    WGu = W | G | u
    WGb = W | G | b
    WGr = W | G | r
    WGub = W | G | u | b
    WGur = W | G | u | r
    WGbr = W | G | b | r
    WGubr = W | G | u | b | r
    # endregion WG

    # region UB
    UB = U | B
    UBw = U | B | w
    UBr = U | B | r
    UBg = U | B | g
    UBwr = U | B | w | r
    UBwg = U | B | w | g
    UBrg = U | B | r | g
    UBwrg = U | B | w | r | g
    # endregion UB

    # region UR
    UR = U | R
    URw = U | R | w
    URb = U | R | b
    URg = U | R | g
    URwb = U | R | w | b
    URwg = U | R | w | g
    URbg = U | R | b | g
    URwbg = U | R | w | b | g
    # endregion UR

    # region UG
    UG = U | G
    UGw = U | G | w
    UGb = U | G | b
    UGr = U | G | r
    UGwb = U | G | w | b
    UGwr = U | G | w | r
    UGbr = U | G | b | r
    UGwbr = U | G | w | b | r
    # endregion UG

    # region BR
    BR = B | R
    BRw = B | R | w
    BRu = B | R | u
    BRg = B | R | g
    BRwu = B | R | w | u
    BRwg = B | R | w | g
    BRug = B | R | u | g
    BRwug = B | R | w | u | g
    # endregion BR

    # region BG
    BG = B | G
    BGw = B | G | w
    BGu = B | G | u
    BGr = B | G | r
    BGwu = B | G | w | u
    BGwr = B | G | w | r
    BGur = B | G | u | r
    BGwur = B | G | w | u | r
    # endregion BG

    # region RG
    RG = R | G
    RGw = R | G | w
    RGu = R | G | u
    RGb = R | G | b
    RGwu = R | G | w | u
    RGwb = R | G | w | b
    RGub = R | G | u | b
    RGwub = R | G | w | u | b
    # endregion RG
    # endregion Two Colour

    # region Three Colour
    WUB = W | U | B
    WUBr = W | U | B | r
    WUBg = W | U | B | g
    WUBrg = W | U | B | r | g

    WUR = W | U | R
    WURb = W | U | R | b
    WURg = W | U | R | g
    WURbg = W | U | R | b | g

    WUG = W | U | G
    WUGb = W | U | G | b
    WUGr = W | U | G | r
    WUGbr = W | U | G | b | r

    WBR = W | B | R
    WBRu = W | B | R | u
    WBRg = W | B | R | g
    WBRug = W | B | R | u | g

    WBG = W | B | G
    WBGu = W | B | G | u
    WBGr = W | B | G | r
    WBGur = W | B | G | u | r

    WRG = W | R | G
    WRGu = W | R | G | u
    WRGb = W | R | G | b
    WRGub = W | R | G | u | b

    UBR = U | B | R
    UBRw = U | B | R | w
    UBRg = U | B | R | g
    UBRwg = U | B | R | w | g

    UBG = U | B | G
    UBGw = U | B | G | w
    UBGr = U | B | G | r
    UBGwr = U | B | G | w | r

    URG = U | R | G
    URGw = U | R | G | w
    URGb = U | R | G | b
    URGwb = U | R | G | w | b

    BRG = B | R | G
    BRGw = B | R | G | w
    BRGu = B | R | G | u
    BRGwu = B | R | G | w | u
    # endregion Three Colour

    # region Four Colour
    WUBR = W | U | B | R
    WUBRg = W | U | B | R | g

    WUBG = W | U | B | G
    WUBGr = W | U | B | G | r

    WURG = W | U | R | G
    WURGb = W | U | R | G | b

    WBRG = W | B | R | G
    WBRGu = W | B | R | G | u

    UBRG = U | B | R | G
    UBRGw = U | B | R | G | w
    # endregion Four Colour

    # region Five Colour
    WUBRG = W | U | B | R | G
    # endregion Five Colour
    # endregion Enumeration Flags

    # region Factory Methods
    @classmethod
    def from_name(cls, colors: ColorCombinationIdentityString) -> ColorCombination:
        """
        Creates a ColorCombination from a ColorCombinationIdentityString.

        :param colors: The string representation of the ColorCombination.
        :return: The ColorCombination.
        """
        # If the name is the empty string, count that as colorless.
        if colors == '':
            return ColorCombination.C

        # ColorAlias should inherently exist in the member map.
        return cls[colors]

    @classmethod
    def from_identities(cls, main: ColorIdentity, splash: ColorIdentity) -> ColorCombination:
        return ColorCombination(main.value + (splash.value << 5))
    # endregion Factory Methods

    # region Instance Functions / Properties
    @property
    def is_valid(self) -> bool:
        """If the ColorCombination is a valid main/splash mix."""
        return (self.value & 31) & (self.value >> 5) == 0

    # region Color Properties
    @property
    def main_color(self) -> ColorIdentity:
        """The ColorIdentity of the main color."""
        return ColorIdentity(self.value & 31)

    @property
    def splash_color(self) -> ColorIdentity:
        """The ColorIdentity of the splash color."""
        return ColorIdentity(self.value >> 5)

    @property
    def colors(self) -> ColorIdentity:
        """The ColorCombination's colors, including splash colors."""
        return self.main_color | self.splash_color

    @property
    def color_string(self) -> ColorIdentityString:
        """The ColorIdentityString for ``main_color``."""
        return self.main_color.wubrg_str

    @property
    def splash_string(self) -> SplashIdentityString:
        """The SplashIdentityString for ``splash_color``."""
        return funcs.color_to_splash(self.splash_color.wubrg_str)

    @property
    def color_count(self) -> int:
        """The number of colours in the ColorIdentity, including splash colors."""
        return self.main_color.color_count + self.splash_color.color_count
    # endregion Color Properties

    # region Index Properties
    @staticmethod
    def _gen_combined_index(idx1: int, idx2: int) -> int:
        """
        This leans on the original sorting indexes of ColorIdentity to create a new
        ordering. To "cheat" having to re-calculate the indexes based on the list of
        ColorCombinationIdentityString, we multiply the ``main_color`` index by 100,
        and add the index of ``splash_color``.

        In base 10, multiplying by 100 shifts the number to the left by two places,
        meaning that adding the ``splash_color`` index to the value doesn't affect
        digits of the ``main_color``. This allows  for the ``main_color`` index to
        take precedence, since each index is only a two-digit number, at most.

        This makes sorting easier (and faster) by only having to compare against
        one value, instead of two.

        :param idx1: The main index to sort on.
        :param idx2: The secondary index to sort on.
        :return: The new sort index.
        """
        return (idx1 * 100) + idx2

    @property
    def wubrg_idx(self) -> int:
        """Generates the sorting index for wubrg order."""
        return self._gen_combined_index(self.main_color.wubrg_idx, self.splash_color.wubrg_idx)

    @property
    def pentad_idx(self) -> int:
        """The sorting index for pentad order."""
        return self._gen_combined_index(self.main_color.pentad_idx, self.splash_color.pentad_idx)

    @property
    def deck_idx(self) -> int:
        """The sorting index for deck building order."""
        # NOTE: Modifying the index to better conform to what people would expect (something with no
        #  splash comes before anything with a splash, even if colorless cards are last). Ignoring
        #  name and cost, this means 'Ambush Paratrooper', 'Chromatic Star', and 'Scrapwork Cohort'
        #  would be in the correct order (colorless last, splashes after no splashes).
        #
        #  Using the above ``_gen_combined_index`` we get a single value, but the colorless splash
        #  has the max index (31). To modify the index so ColorCombination with no splashes come
        #  before any that splash, we subtract the maximum index plus one (32) from val, placing
        #  it as the first element for a main colour.
        #  To preserve index clarity we add 1 to all indexes, so that matching main colours share
        #  the same thousands and hundreds values.
        #  (If we didn't add 1 to everything U.deck_idx -> 99, and Uw.deck_idx -> 100, which is messy.)
        val = self._gen_combined_index(self.main_color.deck_idx, self.splash_color.deck_idx)
        if self.splash_color == ColorIdentity.C:
            val -= len(custom_types.SPLASH_IDENTITIES)
        return val + 1
    # endregion Index Properties

    # region Set-Like Properties
    def merge(self, other: ColorCombination) -> ColorCombination:
        """
        Merges one ColorCombination with another, handling overlapping colours.

        If a colour exists in the main colour and the splash colour, the colour
        in the main colour takes precedence, and the one in the splash is removed.

        Eg: ``WUg, WGb -> WUGb``
        """
        # Merge the two enums together, then use bitwise operations to make
        #  any color that's in the merged enum's WUBRG bits, 0 in the mask's
        #  wubrg bits. Bitwise-and the merged enum and mask to remove
        #  duplicated splash values.
        # Example logic:
        #  g r b u w G R B U W       g r b u w G R B U W       g r b u w G R B U W
        #  1 0 0 0 0 0 0 0 1 1   |   0 0 1 0 0 1 0 0 0 1  -->  1 0 1 0 0 1 0 0 1 1
        #  1 0 1 0 0 1 0 0 1 1  <<5                       -->  1 0 0 1 1 0 0 0 0 0
        #  1 0 0 1 1 0 0 0 0 0   ~                        -->  0 1 1 0 0 1 1 1 1 1
        #  1 0 1 0 0 1 0 0 1 1   &   0 1 1 0 0 1 1 1 1 1  -->  0 0 1 0 0 1 0 0 1 1
        val = (self | other)
        mask = (val & ColorCombination.WUBRG).value << 5
        return val & ColorCombination(~mask)

    @property
    def exact(self) -> list[ColorCombination]:
        """
        Returns a list of ColorCombination which exactly match the ColorCombination.

        Eg: ``WUg -> [WUg]``
        """
        return [self]

    @property
    def subset(self) -> list[ColorCombination]:
        """
        Returns a list of ColorCombination which are a non-strict subset of ColorCombination.

        Eg: ``WUg -> [g, W, Wg, U, Ug, WU, Wug]``
        """
        return [ci for ci in ColorCombination if ci <= self]

    @property
    def superset(self) -> list[ColorCombination]:
        """
        Returns a list of ColorCombination which are a non-strict superset of ColorCombination.

        Eg: ``WUg -> [WUg, WUbg, WUrg, WUbrg, WUBg, WUBrg... WUBRG]``
        """
        return [ci for ci in ColorCombination if ci >= self]

    @property
    def adjacent(self) -> list[ColorCombination]:
        """
        Returns a list of ColorCombination which are no more than one colour different than ColorCombination.

        Eg: ``WUg -> [WUg, Ug, Wg, WUBg, WURg, WUGg, WUwg, WUug, WUbg, WUrg, WU]``
        """
        c = [ColorCombination(0)] + [ColorCombination(2**i) for i in range(0, 10)]
        return [self ^ ci for ci in c]

    @property
    def shares(self) -> list[ColorCombination]:
        """
        Returns a list of ColorCombination which shares any color with ColorCombination.

        Eg: ``WUg -> [W, Wg, U, Ug, WU, WB, WBg... UB, UBg,... WUBRG]``
        """
        return [ci for ci in ColorCombination if (self & ci)]
    # endregion Set-Like Properties

    # region Comparator Functions
    def __eq__(self, other: ColorCombination) -> bool:
        return self.value == other.value

    def __ne__(self, other: ColorCombination) -> bool:
        return not self.__eq__(other)

    def __ge__(self, other: ColorCombination) -> bool:
        return (self.colors >= other.colors) and (self.main_color >= other.main_color)

    def __le__(self, other: ColorCombination) -> bool:
        return (self.colors <= other.colors) and (self.main_color <= other.main_color)

    def __gt__(self, other: ColorCombination) -> bool:
        return (not self.__eq__(other)) and self.__ge__(other)

    def __lt__(self, other: ColorCombination) -> bool:
        return (not self.__eq__(other)) and self.__le__(other)
    # endregion Comparator Functions

    def __iter__(self) -> Iterator[ColorCombination]:
        """Returns an Iterator, with a ColorCombination for color and splash in ColorCombination."""
        temp_str: AnyStr = self.__str__()
        return iter(ColorCombination.from_name(c) for c in temp_str)

    def __str__(self) -> str:
        """A string, which has the character for each flag that is set."""
        if self.name == 'C':
            return ''
        else:
            return self.color_string + self.splash_string

    def __repr__(self) -> str:
        """
        The representation of the ColorCombination, which shows itself as a string,
        along with the reprs of each ColorIdentity (``main_color`` then ``splash_color``).
        """
        return f"'{self}': {self.main_color.__repr__()}, {self.splash_color.__repr__()}"
    # endregion Instance Functions / Properties
