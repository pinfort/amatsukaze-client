from enum import IntEnum, unique


@unique
class FilterFps(IntEnum):
    VFR = 0
    CFR24 = 1
    CFR30 = 2
    CFR60 = 3
    SVP = 4
    VFR30 = 5
