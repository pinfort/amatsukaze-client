from dataclasses import dataclass

from amatsukaze_client.enum.message.service_setting_update_type import (
    ServiceSettingUpdateType,
)
from amatsukaze_client.model.message.service_setting_element import (
    ServiceSettingElement,
)


@dataclass
class ServiceSettingUpdate:
    type: ServiceSettingUpdateType
    service_id: int
    data: ServiceSettingElement
    remove_logo_index: int
