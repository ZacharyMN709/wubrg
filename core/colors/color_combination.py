from typing import cast

from core.colors.color_identity import ColorIdentity
from core.colors.color_typing import ColorIdentityString, SplashIdentityString, ColorCombinationIdentityString


class InvalidColorCombinationException(Exception):
    pass


class ColorCombination:
    main_color: ColorIdentity
    splash_color: ColorIdentity

    def __init__(self, main: ColorIdentityString, splash: SplashIdentityString):
        self.main_color = ColorIdentity.by_name(main)
        self.splash_color = ColorIdentity.by_name(splash.upper())

        if self.main_color & self.splash_color != ColorIdentity.C:
            raise InvalidColorCombinationException("`main_color` and `splash_color` cannot overlap.")

    @property
    def colors(self) -> ColorIdentity:
        """The colors, including splash colors."""
        return self.main_color | self.splash_color

    @property
    def color_string(self) -> ColorIdentityString:
        """The ColorIdentityString for `main_color`."""
        return cast(ColorIdentityString, str(self.main_color))

    @property
    def splash_string(self) -> SplashIdentityString:
        """The SplashIdentityString for `splash_color`."""
        return cast(SplashIdentityString, str(self.splash_color).lower())

    def __str__(self) -> ColorCombinationIdentityString:
        """The ColorCombinationIdentityString for the instance."""
        return cast(ColorCombinationIdentityString, self.color_string + self.splash_string)

    def __repr__(self) -> str:
        """The representation of the object, which shows itself as a string, with the reprs of each ColorIdentity."""
        return f"'{self}': {self.main_color.__repr__()}, {self.splash_color.__repr__()}"
