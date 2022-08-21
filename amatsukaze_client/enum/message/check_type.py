from enum import IntEnum, unique


@unique
class CheckType(IntEnum):
    DRCS = 0,
    CM = 1,
