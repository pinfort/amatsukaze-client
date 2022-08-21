from enum import Enum, auto, unique


@unique
class StateChangeEvent(Enum):
    WORKERS_STARTED = auto()
    WORKERS_FINISHED = auto()
    ENCODE_STARTED = auto()
    ENCODE_SUCCEEDED = auto()
    ENCODE_FAILED = auto()
    ENCODE_CHACELED = auto()
