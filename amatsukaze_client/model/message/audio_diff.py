from dataclasses import dataclass


@dataclass
class AudioDiff:
    total_src_frames: int
    total_out_frames: int
    total_out_unique_frames: int
    not_included_per: float
    avg_diff: float
    max_diff: float
    max_diff_pos: float
