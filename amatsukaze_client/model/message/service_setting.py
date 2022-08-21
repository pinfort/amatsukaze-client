from dataclasses import dataclass
from typing import Dict

from amatsukaze_client.model.message.service_setting_element import (
    ServiceSettingElement,
)


@dataclass
class ServiceSetting:
    service_map: Dict[int, ServiceSettingElement]

    # extension_data: ? どうするか考える
