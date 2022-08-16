from enum import IntEnum, unique


@unique
class DecoderType(IntEnum):
    DEFAULT = 0,
    QSV = 1,
    CUVID = 2,
