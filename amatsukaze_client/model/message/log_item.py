import os
from dataclasses import dataclass
from datetime import datetime, timedelta
from tkinter.messagebox import NO
from typing import Iterable, List, Union

from amatsukaze_client.model.message.audio_diff import AudioDiff
from amatsukaze_client.model.message.error_count import ErrorCount


@dataclass
class LogItem:
    src_path: str
    success: bool
    dst_path: str
    out_path: List[str]
    encode_start_date: datetime
    encode_finish_date: datetime
    src_video_duration: timedelta
    out_video_duration: timedelta
    src_file_size: int
    int_video_file_size: int
    out_file_size: int
    audio_diff: AudioDiff
    reason: str
    machine_name: str
    logo_files: List[str]

    chapter: bool
    nico_jk: bool
    trim_avs: bool
    output_mask: int
    service_name: str
    service_id: int
    ts_time: datetime

    incident: int
    error: List[ErrorCount]

    profile: str

    tags: List[str]

    # extension_data: ? どうするか考える

    @property
    def encode_duration(self) -> timedelta:
        return self.encode_finish_date - self.encode_start_date

    @property
    def display_result(self) -> str:
        if not self.success:
            return "x"
        if self.incident > 0:
            return "△"
        else:
            return "〇"

    @property
    def display_src_directory(self) -> str:
        return os.path.dirname(self.src_path)

    @property
    def display_src_filename(self) -> str:
        return os.path.basename(self.src_path)

    @property
    def display_out_directory(self) -> Union[str, None]:
        if self.out_path is not None and self.out_path.count() > 0:
            return os.path.dirname(self.out_path[0])
        return "-"

    @property
    def display_out_file(self) -> Union[Iterable[str], None]:
        if self.out_path is None:
            return None
        return [os.path.basename(s) for s in self.out_path]

    @property
    def display_out_num(self) -> str:
        if self.out_path is None:
            return "-"
        else:
            return str(self.out_path.count())

    @property
    def display_num_incident(self) -> str:
        return str(self.incident)

    @property
    def display_encode_start(self) -> str:
        return self.encode_start_date.strftime("%Y/%m/%d %H:%M:%S")

    @property
    def display_encode_finish(self) -> str:
        return self.encode_finish_date.strftime("%Y/%m/%d %H:%M:%S")

    @property
    def display_encode_duration(self) -> str:
        mm, ss = divmod(self.encode_duration.seconds, 60)
        hh, mm = divmod(mm, 60)
        hours: int = self.encode_duration.days * 24 + hh
        return "{hours}時間{minutes:02}分{seconds:02}秒".format(
            hours=hours, minutes=mm, seconds=ss
        )

    @property
    def display_src_duration(self) -> Union[str, None]:
        if self.src_video_duration is None:
            return None
        else:
            mm, ss = divmod(self.src_video_duration.seconds, 60)
            hh, mm = divmod(mm, 60)
            hours: int = self.src_video_duration.days * 24 + hh
            return "{hours}時間{minutes:02}分{seconds:02}秒".format(
                hours=hours, minutes=mm, seconds=ss
            )

    @property
    def display_out_duration(self) -> str:
        if self.out_video_duration is None:
            return None
        else:
            mm, ss = divmod(self.out_video_duration.seconds, 60)
            hh, mm = divmod(mm, 60)
            hours: int = self.out_video_duration.days * 24 + hh
            return "{hours}時間{minutes:02}分{seconds:02}秒".format(
                hours=hours, minutes=mm, seconds=ss
            )

    @property
    def display_video_not_included(self) -> Union[str, None]:
        if self.src_video_duration is None:
            return None
        difference_of_durations: timedelta = (
            self.src_video_duration - self.out_video_duration
        )
        percentage: float = (
            difference_of_durations.total_seconds()
            * 100
            / self.src_video_duration.total_seconds()
        )
        return format(percentage, ".2f")

    @property
    def diplay_src_file_size(self) -> str:
        return format(self.src_file_size / (1024 * 1024), ".2f")

    @property
    def display_int_file_size(self) -> str:
        return format(self.int_video_file_size / (1024 * 1024), ".2f")

    @property
    def display_out_file_size(self) -> str:
        return format(self.out_file_size / (1024 * 1024), ".2f")

    @property
    def display_int_video_rate(self) -> str:
        return format(self.int_video_file_size * 100 / self.src_file_size, ".2f")

    @property
    def display_compression_rate(self) -> str:
        return format(self.out_file_size * 100 / self.src_file_size, ".2f")

    @property
    def display_src_audio_frames(self) -> Union[str, None]:
        if self.audio_diff is None:
            return None
        else:
            return str(self.audio_diff.total_src_frames)

    @property
    def display_out_audio_frames(self) -> Union[str, None]:
        if self.audio_diff is None:
            return None
        else:
            return str(self.audio_diff.total_out_frames)

    @property
    def display_audio_not_included(self) -> Union[str, None]:
        if self.audio_diff is None:
            return None
        else:
            return format(self.audio_diff.not_included_per, ".3f")

    @property
    def display_avg_audio_diff(self) -> Union[str, None]:
        if self.audio_diff is None:
            return None
        else:
            return format(self.audio_diff.avg_diff, ".2f")

    @property
    def display_reason(self) -> str:
        return self.reason

    @property
    def display_audio_max_diff(self) -> Union[str, None]:
        if self.audio_diff is None:
            return None
        else:
            format(self.audio_diff.max_diff, ".2f")

    @property
    def display_audio_max_diff_pos(self) -> Union[str, None]:
        if self.audio_diff is None:
            return None
        else:
            format(self.audio_diff.max_diff_pos, ".2f")

    @property
    def display_encode_speed(self) -> Union[str, None]:
        if self.src_video_duration is None:
            return None
        else:
            return format(
                self.src_video_duration.total_seconds()
                / self.encode_duration.total_seconds(),
                ".2f",
            )

    @property
    def display_src_bitrate(self) -> Union[str, None]:
        if self.src_video_duration is None:
            return None
        else:
            format(
                self.src_file_size
                / (self.src_video_duration.total_seconds() * 128 * 1024),
                ".3f",
            )

    @property
    def display_out_bitrate(self) -> Union[str, None]:
        if self.src_video_duration is None:
            return None
        else:
            return format(
                self.out_file_size
                / (self.out_video_duration.total_seconds() * 128 * 1024),
                ".3f",
            )

    @property
    def display_logo(self) -> str:
        return next(iter(self.logo_files), "なし")

    @property
    def display_chapter(self) -> str:
        if self.chapter:
            return "○"
        else:
            return "☓"

    @property
    def display_nico_jk(self) -> str:
        if self.nico_jk:
            return "○"
        else:
            return "☓"

    @property
    def display_trim_avs(self) -> str:
        if self.trim_avs:
            return "○"
        else:
            return "☓"

    @property
    def display_output_mask(self) -> str:
        if self.output_mask == 1:
            return "通常"
        elif self.output_mask == 2:
            return "CMをカット"
        elif self.output_mask == 3:
            return "通常+CMをカット"
        elif self.output_mask == 4:
            return "CMのみ"
        elif self.output_mask == 5:
            return "通常+CM"
        elif self.output_mask == 6:
            return "本編とCMを分離"
        elif self.output_mask == 7:
            return "通常+本編+CM"
        else:
            return "通常"

    @property
    def display_service(self) -> str:
        return f"{self.service_name}({self.service_id})"

    @property
    def display_ts_time(self) -> str:
        if self.ts_time == datetime.min:
            return "不明"
        return self.ts_time.strftime("%Y年%m月%d日")

    @property
    def display_tags(self) -> str:
        if self.tags is None:
            return None
        return " ".join(self.tags)
