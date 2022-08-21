from dataclasses import dataclass
from typing import List

from amatsukaze_client.model.message.drcs_source_item import DrcsSourceItem

@dataclass
class DrcsImage():
    md5: str
    map_str: str
    source_list: List[DrcsSourceItem]

    # image: BitmapFrame どうするか考える
