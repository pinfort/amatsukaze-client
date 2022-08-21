from dataclasses import dataclass
from datetime import datetime, timedelta
import os
from typing import List

from amatsukaze_client.enum.message.proc_mode import ProcMode
from amatsukaze_client.model.message.profile_setting import ProfileSetting
from amatsukaze_client.enum.message.queue_state import QueueState
from amatsukaze_client.model.message.genre_item import GenreItem

@dataclass
class QueueItem():
    id: int
    mode: ProcMode
    profile: ProfileSetting
    src_path: str
    dst_path: str
    hash: bytes
    state: QueueState
    priority: int
    add_time: datetime

    service_id: int
    service_name: str
    image_width: int
    image_height: int
    ts_time: datetime

    fail_reason: str
    jls_command: str

    profile_name: str
    event_name: str
    genre: List[GenreItem]
    actual_dst_path: str
    console_id: int

    encode_start: datetime
    encode_time: timedelta

    tags: List[str]

    # 内部処理順決定用パラメータ
    order: int

    @property
    def encode_finish(self) -> datetime:
        if self.encode_start == datetime.min or self.encode_time == timedelta(0,0,0,0,0,0,0):
            return datetime.min
        return self.encode_start + self.encode_time

    @property
    def is_batch(self) -> bool:
        return self.mode == ProcMode.BATCH or self.mode == ProcMode.AUTO_BATCH
    
    @property
    def is_check(self) -> bool:
        return self.mode == ProcMode.DRCS_CHECK or self.mode == ProcMode.CM_CHECK

    @property
    def is_test(self) -> bool:
        return self.mode == ProcMode.TEST
    
    @property
    def dir_name(self) -> str:
        return os.path.dirname(self.src_path)
    
    @property
    def file_name(self) -> str:
        return os.path.basename(self.src_path)
    
    @property
    def is_active(self) -> bool:
        return self.state == QueueState.ENCODING \
            or self.state == QueueState.LOGO_PENDING \
            or self.state == QueueState.QUEUE

    @property
    def is_one_seg(self) -> bool:
        return self.image_width <= 320 \
            or self.image_height <= 260

    @property
    def is_separate_hash_required(self) -> bool:
        return self.mode == ProcMode.BATCH \
            and self.profile.disable_hash_check == False \
            and self.src_path.startswith("\\\\")

    def reset(self) -> None:
        self.state = QueueState.LOGO_PENDING
        self.encode_start = datetime.min
        self.encode_time = timedelta(0,0,0,0,0,0,0)
