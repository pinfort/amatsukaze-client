from dataclasses import dataclass
from typing import Union


@dataclass
class AddQueueItem:
    path: str
    hash: Union[bytes, None]
