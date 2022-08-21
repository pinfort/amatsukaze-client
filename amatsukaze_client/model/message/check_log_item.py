from dataclasses import dataclass
from datetime import datetime, timedelta
import os

from amatsukaze_client.enum.message.check_type import CheckType

@dataclass
class CheckLogItem():
    type: CheckType
    src_path: str
    success: bool
    check_start_date: datetime
    check_finish_date: datetime
    profile: str
    service_name: str
    service_id: int
    ts_time: datetime
    reason: str
    # extension_data: ? どうするか考える

    @property
    def display_type(self) -> str:
        if self.type == CheckType.CM:
            return "CM解析"
        elif self.type == CheckType.DRCS:
            return "DRCSチェック"
        else:
            return "不明"
    
    @property
    def encode_duration(self) -> timedelta:
        return self.check_finish_date - self.check_start_date
    
    @property
    def display_result(self) -> str:
        return "〇" if self.success else "x"
    
    @property
    def display_src_directory(self) -> str:
        return os.path.dirname(self.src_path)
    
    @property
    def display_src_filename(self) -> str:
        return os.path.basename(self.src_path)
    
    @property
    def display_encode_start(self) -> str:
        return self.check_start_date.strftime("%Y/%m/%d %H:%M:%S")
    
    @property
    def display_encode_finish(self) -> str:
        return self.check_finish_date.strftime("%Y/%m/%d %H:%M:%S")
    
    @property
    def display_encode_duration(self) -> str:
        mm, ss = divmod(self.encode_duration.seconds, 60)
        hh, mm = divmod(mm, 60)
        hours: int = self.encode_duration.days * 24 + hh
        return "{hours}時間{minutes:02}分{seconds:02}秒".format(hours=hours, minutes=mm, seconds=ss)

    @property
    def display_reason(self) -> str:
        return self.reason

    @property
    def display_service(self) -> str:
        return f"{self.service_name}({self.service_id})"

    @property
    def display_ts_time(self) -> str:
        return "不明" if self.ts_time == datetime.min else self.ts_time.strftime("%Y年%m月%d日")
