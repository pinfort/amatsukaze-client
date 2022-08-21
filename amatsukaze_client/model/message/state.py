from dataclasses import dataclass
from typing import List


@dataclass
class State():
    pause: bool
    suspend: bool
    encoder_suspend: List[bool]
    running: bool
    scheduled_pause: bool
    scheduled_suspend: bool
    progress: float
