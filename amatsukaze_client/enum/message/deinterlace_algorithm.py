from enum import IntEnum, unique


@unique
class DeinterlaceAlgorithm(IntEnum):
    KFM = 0,
    D3DVP = 1,
    QTGMC = 2,
    YADIF = 3,
    AUTO_VFR = 4,
