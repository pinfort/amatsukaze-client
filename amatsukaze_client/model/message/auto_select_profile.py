from dataclasses import dataclass
from typing import List

from amatsukaze_client.model.message.auto_select_condition import AutoSelectCondition

@dataclass
class AutoSelectProfile():
    name: str
    conditions: List[AutoSelectCondition]
