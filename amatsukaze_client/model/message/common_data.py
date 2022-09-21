from dataclasses import dataclass
from typing import List

from amatsukaze_client.model.message.disk_item import DiskItem
from amatsukaze_client.model.message.finish_setting import FinishSetting
from amatsukaze_client.model.message.make_script_data import MakeScriptData
from amatsukaze_client.model.message.server_info import ServerInfo
from amatsukaze_client.model.message.setting import Setting
from amatsukaze_client.model.message.ui_state import UiState


@dataclass
class CommonData:
    ui_state: UiState
    setting: Setting
    make_script_data: MakeScriptData
    jls_command_files: List[str]
    main_script_files: List[str]
    post_script_files: List[str]
    disks: List[DiskItem]
    cpu_clusters: List[int]
    server_info: ServerInfo
    add_queue_bat_files: List[str]
    pre_bat_files: List[str]
    post_bat_files: List[str]
    finish_setting: FinishSetting
