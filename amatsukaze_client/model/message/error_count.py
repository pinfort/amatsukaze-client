from dataclasses import dataclass


@dataclass
class ErrorCount():
    name: str
    count: int

    # extension_data: ? どうするか考える
