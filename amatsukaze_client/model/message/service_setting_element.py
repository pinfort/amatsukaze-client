from dataclasses import dataclass
from typing import List

from amatsukaze_client.model.message.logo_setting import LogoSetting


@dataclass
class ServiceSettingElement:
    service_id: int
    service_name: str
    disable_cm_check: bool
    jls_command: str
    jls_option: str
    logo_settings: List[LogoSetting]

    # extension_data: ? どうするか考える
