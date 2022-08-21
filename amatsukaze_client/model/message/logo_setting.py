from dataclasses import dataclass
from datetime import datetime

@dataclass
class LogoSetting():
    exists: bool
    file_name: str
    logo_name: str
    service_id: int
    enabled: bool
    from_datetime: datetime # fromという名前は使えないので仕方なく名前を変えている
    to: datetime

    def can_use(self, ts_time: datetime) -> bool:
        return self.exists and self.enabled and (
            ts_time == datetime.min
            or (
                self.from_datetime <= ts_time
                and ts_time <= self.to
            )
        )
    
    # extension_data: ? どうするか考える

    @property
    def NO_LOGO(self) -> str:
        return "### NO LOGO ###"
