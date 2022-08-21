from dataclasses import dataclass
from typing import List


@dataclass
class Setting():
    amatsukaze_path: str
    x264_path: str
    x265_path: str
    qsvenc_path: str
    nvenc_path: str
    vceenc_path: str
    svtav1_path: str
    muxer_path: str
    mkv_merge_path: str
    mp4_box_path: str
    timeline_editor_path: str
    chapter_exe_path: str
    join_logo_scp_path: str
    nico_conv_ass_path: str
    ts_muxer_path: str
    scr_rename_path: str
    auto_vfr_path: str
    nero_aac_enc_path: str
    qaac_path: str
    fdkaac_path: str

    work_path: str
    always_show_disk: str

    num_parallel: int
    affinity_setting: int
    process_priority: int

    clear_work_dir_on_start: bool
    hide_one_seg: bool
    list_style: int
    supress_sleep: bool
    dump_filter: bool
    scheduling_enabled: bool
    num_gpu: int
    max_gpu_resources: List[int]

    enable_x265_vfr_time_factor: bool
    x265_vfr_time_factor: float

    pause_on_started: bool
    print_time_prefix: bool
    enable_shutdown_action: bool

    enable_run_hours: bool
    run_hours_suspend_encoders: bool
    run_hours: List[bool]

    # extension_data: ? どうするか考える

    @property
    def actual_work_path(self) -> str:
        return "./" if len(self.work_path) == 0 else self.work_path

    # どうするか考える
    # @property
    # def process_priority_class(self) -> ?:
