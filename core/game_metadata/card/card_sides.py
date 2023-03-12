from typing import Literal
from enum import Enum, auto


# region Card Layouts
CARD_SIDE = Literal['default', 'main', 'adventure', 'left', 'right', 'front', 'back', 'flipped', 'melded', 'prototype']


# https://scryfall.com/docs/api/layouts
class CardLayouts(Enum):
    NORMAL = auto()
    SPLIT = auto()
    FLIP = auto()
    TRANSFORM = auto()
    MODAL_DFC = auto()
    MELD = auto()
    LEVELER = auto()
    CLASS = auto()
    SAGA = auto()
    ADVENTURE = auto()
    PROTOTYPE = auto()

    BASIC = NORMAL | LEVELER | CLASS | SAGA
    FUSED = ADVENTURE | SPLIT | FLIP | PROTOTYPE
    TWO_SIDED = TRANSFORM | MODAL_DFC | MELD


LAYOUT_DICT: dict[str, CardLayouts] = {
    "normal": CardLayouts.NORMAL,
    "split": CardLayouts.SPLIT,
    "flip": CardLayouts.FLIP,
    "transform": CardLayouts.TRANSFORM,
    "modal_dfc": CardLayouts.MODAL_DFC,
    "meld": CardLayouts.MELD,
    "leveler": CardLayouts.LEVELER,
    "class": CardLayouts.CLASS,
    "saga": CardLayouts.SAGA,
    "adventure": CardLayouts.ADVENTURE,
    "prototype": CardLayouts.PROTOTYPE,
}
# endregion Card Layouts
