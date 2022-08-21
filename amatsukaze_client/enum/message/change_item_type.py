from enum import IntEnum, unique


@unique
class ChangeItemType(IntEnum):
    RESET_STATE = 0,
    UPDATE_PROFILE = 1,
    DUPLICATE = 2,
    CANCEL = 3,
    PRIORITY = 4,
    PROFILE = 5,
    REMOVE_ITEM = 6,
    REMOVE_COMPLETED = 7,
    FORCE_RESTART = 8,
    REMOVE_SOURCE_FILE = 9,
    MOVE = 10,
