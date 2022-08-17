from dataclasses import dataclass
from typing import List

from amatsukaze_client.model.message.queue_item import QueueItem

@dataclass
class QueueData():
    items: List[QueueItem]
