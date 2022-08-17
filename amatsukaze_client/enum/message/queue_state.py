from enum import IntEnum, unique


@unique
class QueueState(IntEnum):
    QUEUE = 0,
    ENCODING = 1,
    COMPLETE = 2,
    FAILED = 3,
    PRE_FAILED = 4,
    LOGO_PENDING = 5,
    CANCELED = 6,
