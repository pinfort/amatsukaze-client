from dataclasses import dataclass
from typing import List


@dataclass
class UiState():
    last_used_profile: str
    last_output_path: str
    last_add_queue_bat: str
    output_path_history: List[str]

    # extension_data: ? どうするか考える
