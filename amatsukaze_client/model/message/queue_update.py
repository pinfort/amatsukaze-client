from dataclasses import dataclass

from amatsukaze_client.enum.message.update_type import UpdateType
from amatsukaze_client.model.message.queue_item import QueueItem


@dataclass
class QueueUpdate:
    type: UpdateType
    item: QueueItem
    position: int
