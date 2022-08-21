from dataclasses import dataclass


@dataclass
class BitrateSetting():
    a: float
    b: float
    h264: float
    # extension_data: ? どうするか検討
