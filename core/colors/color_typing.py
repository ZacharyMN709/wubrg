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
