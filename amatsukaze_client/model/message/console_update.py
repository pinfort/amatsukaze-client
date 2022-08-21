from dataclasses import dataclass


@dataclass
class ConsoleUpdate():
    index: int
    data: bytes
