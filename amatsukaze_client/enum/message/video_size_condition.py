from enum import Enum, auto, unique


@unique
class VideoSizeCondition(Enum):
    FULL_HD = auto(),
    HD1440 = auto(),
    SD = auto(),
    ONE_SEG = auto(),
