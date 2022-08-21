from dataclasses import dataclass
from typing import List

from amatsukaze_client.model.message.genre_item import GenreItem
from amatsukaze_client.enum.message.video_size_condition import VideoSizeCondition

@dataclass
class AutoSelectCondition():
    file_name_enabled: bool
    file_name: str
    content_condition_enabled: bool
    content_conditions: List[GenreItem]
    service_id_enabled: bool
    service_ids: List[int]
    video_size_enabled: bool
    video_sizes: List[VideoSizeCondition]
    tag_enabled: bool
    tag: str
    profile: str
    priority: int
    description: str
