from dataclasses import dataclass
from typing import List

from amatsukaze_client.model.message.log_item import LogItem

@dataclass
class LogData():
    items: List[LogItem]
    # extension_data: ? どうするか考える
