from enum import Enum, auto, unique


@unique
class DrcsUpdateType(Enum):
    REMOVE = auto()
    UPDATE = auto()
