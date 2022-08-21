from ctypes import Union
from dataclasses import dataclass

from amatsukaze_client.model.message.state import State
from amatsukaze_client.model.message.queue_data import QueueData
from amatsukaze_client.model.message.queue_update import QueueUpdate
from amatsukaze_client.model.message.log_data import LogData
from amatsukaze_client.model.message.log_item import LogItem
from amatsukaze_client.model.message.check_log_data import CheckLogData
from amatsukaze_client.model.message.check_log_item import CheckLogItem
from amatsukaze_client.model.message.console_data import ConsoleData
from amatsukaze_client.model.message.encode_state import EncodeState
from amatsukaze_client.model.message.finish_setting import FinishSetting
from amatsukaze_client.enum.message.state_change_event import StateChangeEvent


@dataclass
class UIData:
    state: State
    queue_data: QueueData
    queue_update: QueueUpdate
    log_data: LogData
    log_item: LogItem
    check_log_data: CheckLogData
    check_log_item: CheckLogItem
    console_data: ConsoleData
    encode_state: EncodeState
    sleep_cancel: FinishSetting
    state_change_event: Union[StateChangeEvent, None]
