from enum import IntEnum, unique


@unique
class DeblockStrength(IntEnum):
    STRONG = 0,
    MIDIUM = 1,
    WEAK = 2,
    WEAKER = 3,
