from enum import IntEnum, unique


@unique
class QtgmcPreset(IntEnum):
    AUTO = 0
    FASTER = 1
    FAST = 2
    MEDIUM = 3
    SLOW = 4
    SLOWER = 5
