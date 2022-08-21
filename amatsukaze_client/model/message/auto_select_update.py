from dataclasses import dataclass

from amatsukaze_client.enum.message.update_type import UpdateType
from amatsukaze_client.model.message.auto_select_profile import AutoSelectProfile


@dataclass
class AutoSelectUpdate:
    type: UpdateType
    profile: AutoSelectProfile
    new_name: str
