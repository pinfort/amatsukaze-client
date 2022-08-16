from enum import IntEnum, unique


@unique
class AudioEncoderType(IntEnum):
    NEROAAC = 0,
    QAAC = 1,
    FDKAAC = 2,
