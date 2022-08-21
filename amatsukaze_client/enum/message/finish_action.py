from enum import IntEnum, unique


@unique
class FinishAction(IntEnum):
    NONE = 0,
    SUSPEND = 1,
    HIBERNATE = 2,
    SHUTDOWN = 3,
