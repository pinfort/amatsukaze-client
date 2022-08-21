from dataclasses import dataclass
from datetime import datetime, timedelta


@dataclass
class DrcsSourceItem():
    file_name: str
    found_time: datetime
    elapsed: timedelta

    def __str__(self) -> str:
        mm, ss = divmod(self.elapsed.seconds, 60)
        hh, mm = divmod(mm, 60)
        hours: int = self.elapsed.days * 24 + hh
        return "{hours}:{minutes:02}:{seconds:02}@{file_name}".format(hours=hours, minutes=mm, seconds=ss, file_name=self.file_name)
