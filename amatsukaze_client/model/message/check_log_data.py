from dataclasses import dataclass
from typing import List

from amatsukaze_client.model.message.check_log_item import CheckLogItem

@dataclass
class CheckLogData():
    items: List[CheckLogItem]
    # extension_data: ? どうするか考える
