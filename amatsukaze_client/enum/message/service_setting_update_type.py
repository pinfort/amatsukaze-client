from enum import Enum, auto, unique


@unique
class ServiceSettingUpdateType(Enum):
    UPDATE = auto()
    ADD_NO_LOGO = auto()
    REMOVE = auto()
    REMOVE_LOGO = auto()
    CLEAR = auto()
