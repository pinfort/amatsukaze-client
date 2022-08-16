from enum import IntEnum, unique


@unique
class UpdateType(IntEnum):
    ADD = 0,
    REMOVE = 1,
    UPDATE = 2,
    CLEAR = 3,
    MOVE = 4,
