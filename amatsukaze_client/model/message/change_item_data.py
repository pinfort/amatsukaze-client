from dataclasses import dataclass

from amatsukaze_client.enum.message.change_item_type import ChangeItemType


@dataclass
class ChangeItemData:
    item_id: int
    change_type: ChangeItemType
    priority: int
    profile: str
    position: int
