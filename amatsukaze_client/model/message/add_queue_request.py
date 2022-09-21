from dataclasses import dataclass
from typing import List

from amatsukaze_client.enum.message.proc_mode import ProcMode
from amatsukaze_client.model.message.add_queue_item import AddQueueItem
from amatsukaze_client.model.message.output_info import OutputInfo


@dataclass
class AddQueueRequest:
    dir_path: str
    targets: List[AddQueueItem]
    mode: ProcMode
    outputs: List[OutputInfo]
    request_id: str
    add_queue_bat: str

    @property
    def is_batch(self) -> bool:
        return self.mode == ProcMode.BATCH or self.mode == ProcMode.AUTO_BATCH

    @property
    def is_check(self) -> bool:
        return self.mode == ProcMode.DRCS_CHECK or self.mode == ProcMode.CM_CHECK
