from enum import IntEnum, unique


@unique
class D3dvpgpu(IntEnum):
    AUTO = 0
    INTEL = 1
    NVIDIA = 2
    RADEON = 3
