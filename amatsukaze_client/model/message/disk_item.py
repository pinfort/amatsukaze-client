from dataclasses import dataclass


@dataclass
class DiskItem:
    path: str
    capacity: int
    free: int
