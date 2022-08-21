from enum import IntEnum, unique


@unique
class ProcMode(IntEnum):
    BATCH = 0
    AUTO_BATCH = 1
    TEST = 2
    DRCS_CHECK = 3
    CM_CHECK = 4
