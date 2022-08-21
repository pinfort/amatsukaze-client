from enum import Enum, auto, unique


@unique
class ResourcePhase(Enum):
    TS_ANALYZE = auto()
    CM_ANALYZE = auto()
    FILTER = auto()
    ENCODE = auto()
    MUX = auto()
    MAX = auto()

    NO_WAIT = 0x100
