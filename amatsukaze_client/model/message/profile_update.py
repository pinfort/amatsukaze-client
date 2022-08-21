from dataclasses import dataclass

from amatsukaze_client.enum.message.update_type import UpdateType
from amatsukaze_client.model.message.profile_setting import ProfileSetting


@dataclass
class ProfileUpdate:
    type: UpdateType
    profile: ProfileSetting
    new_name: str
