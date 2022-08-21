from enum import IntEnum, unique


@unique
class FilterOption(IntEnum):
    NONE = 0
    SETTING = 1
    CUSTOM = 2
