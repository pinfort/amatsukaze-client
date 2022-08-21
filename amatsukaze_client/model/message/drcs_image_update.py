from dataclasses import dataclass
from typing import List

from amatsukaze_client.enum.message.drcs_update_type import DrcsUpdateType
from amatsukaze_client.model.message.drcs_image import DrcsImage

@dataclass
class DrcsImageUpdate():
    type: DrcsUpdateType
    image: DrcsImage
    image_list: List[DrcsImage]
