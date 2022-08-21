from dataclasses import dataclass


@dataclass
class OutputInfo:
    dst_path: str
    profile: str
    priority: int
