from dataclasses import dataclass

from amatsukaze_client.model.message.log_item import LogItem
from amatsukaze_client.model.message.check_log_item import CheckLogItem

@dataclass
class LogFileRequest():
    log_item: LogItem
    check_log_item: CheckLogItem
