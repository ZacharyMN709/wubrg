from typing import Literal


ColorString = Literal['W', 'U', 'B', 'R', 'G']

SplashString = Literal['w', 'u', 'b', 'r', 'g']

ColorIdentityString = Literal[
    '', 'W', 'U', 'B', 'R', 'G',
    'WU', 'WB', 'WR', 'WG', 'UB', 'UR', 'UG', 'BR', 'BG', 'RG',
    'WUB', 'WUR', 'WUG', 'WBR', 'WBG', 'WRG', 'UBR', 'UBG', 'URG', 'BRG',
    'WUBR', 'WUBG', 'WURG', 'WBRG', 'UBRG', 'WUBRG'
]

SplashIdentityString = Literal[
    '', 'w', 'u', 'b', 'r', 'g',
    'wu', 'wb', 'wr', 'wg', 'ub', 'ur', 'ug', 'br', 'bg', 'rg',
    'wub', 'wur', 'wug', 'wbr', 'wbg', 'wrg', 'ubr', 'ubg', 'urg', 'brg',
    'wubr', 'wubg', 'wurg', 'wbrg', 'ubrg', 'wubrg'
]

ColorCombinationIdentityString = Literal[
    "W", "Wu", "Wb", "Wr", "Wg", "Wub", "Wur", "Wug", "Wbr", "Wbg", "Wrg", "Wubr", "Wubg", "Wurg", "Wbrg", "Wubrg",
    "U", "Uw", "Ub", "Ur", "Ug", "Uwb", "Uwr", "Uwg", "Ubr", "Ubg", "Urg", "Uwbr", "Uwbg", "Uwrg", "Ubrg", "Uwbrg",
    "B", "Bw", "Bu", "Br", "Bg", "Bwu", "Bwr", "Bwg", "Bur", "Bug", "Brg", "Bwur", "Bwug", "Bwrg", "Burg", "Bwurg",
    "R", "Rw", "Ru", "Rb", "Rg", "Rwu", "Rwb", "Rwg", "Rub", "Rug", "Rbg", "Rwub", "Rwug", "Rwbg", "Rubg", "Rwubg",
    "G", "Gw", "Gu", "Gb", "Gr", "Gwu", "Gwb", "Gwr", "Gub", "Gur", "Gbr", "Gwub", "Gwur", "Gwbr", "Gubr", "Gwubr",
    "WU", "WUb", "WUr", "WUg", "WUbr", "WUbg", "WUrg", "WUbrg",
    "WB", "WBu", "WBr", "WBg", "WBur", "WBug", "WBrg", "WBurg",
    "WR", "WRu", "WRb", "WRg", "WRub", "WRug", "WRbg", "WRubg",
    "WG", "WGu", "WGb", "WGr", "WGub", "WGur", "WGbr", "WGubr",
    "UB", "UBw", "UBr", "UBg", "UBwr", "UBwg", "UBrg", "UBwrg",
    "UR", "URw", "URb", "URg", "URwb", "URwg", "URbg", "URwbg",
    "UG", "UGw", "UGb", "UGr", "UGwb", "UGwr", "UGbr", "UGwbr",
    "BR", "BRw", "BRu", "BRg", "BRwu", "BRwg", "BRug", "BRwug",
    "BG", "BGw", "BGu", "BGr", "BGwu", "BGwr", "BGur", "BGwur",
    "RG", "RGw", "RGu", "RGb", "RGwu", "RGwb", "RGub", "RGwub",
    "WUB", "WUBr", "WUBg", "WUBrg",
    "WUR", "WURb", "WURg", "WURbg",
    "WUG", "WUGb", "WUGr", "WUGbr",
    "WBR", "WBRu", "WBRg", "WBRug",
    "WBG", "WBGu", "WBGr", "WBGur",
    "WRG", "WRGu", "WRGb", "WRGub",
    "UBR", "UBRw", "UBRg", "UBRwg",
    "UBG", "UBGw", "UBGr", "UBGwr",
    "URG", "URGw", "URGb", "URGwb",
    "BRG", "BRGw", "BRGu", "BRGwu",
    "WUBR", "WUBRg",
    "WUBG", "WUBGr",
    "WURG", "WURGb",
    "WBRG", "WBRGu",
    "UBRG", "UBRGw",
    "WUBRG",
]
