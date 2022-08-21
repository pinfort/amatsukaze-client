from enum import IntEnum, unique


@unique
class EncoderType(IntEnum):
    X264 = 0,
    X265 = 1,
    QSVEnc = 2,
    NVEnc = 3,
    VCEENC = 4,
    SVTAV1 = 5,
