from enum import IntEnum, unique


@unique
class FormatType(IntEnum):
    MP4 = 0,
    MKV = 1,
    M2TS = 2,
    TS = 3,
