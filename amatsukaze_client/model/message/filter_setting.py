from dataclasses import dataclass

from amatsukaze_client.enum.message.deblock_strength import DeblockStrength
from amatsukaze_client.enum.message.deinterlace_algorithm import DeinterlaceAlgorithm
from amatsukaze_client.enum.message.d3dvpgpu import D3dvpgpu
from amatsukaze_client.enum.message.qtgmc_preset import QtgmcPreset
from amatsukaze_client.enum.message.filter_fps import FilterFps

@dataclass
class FilterSetting():
    enable_cuda: bool
    enable_deblock: bool
    deblock_quality: int
    deblock_strength: DeblockStrength
    deblock_sharpen: bool
    enable_deinterlace: bool
    deinterlace_algorithm: DeinterlaceAlgorithm
    d3dvp_gpu: D3dvpgpu
    qtgmc_preset: QtgmcPreset
    kfm_enable_nr: bool
    kfm_enable_ucf: bool
    kfm_vfr_120fps: bool
    kfm_fps: FilterFps
    yadif_fps: FilterFps
    auto_vfr_parallel: int
    auto_vfr_fast: bool
    auto_vfr_30f: bool
    auto_vfr_60f: bool
    auto_vfr_24a: bool
    auto_vfr_30a: bool
    auto_vfr_crop: bool
    auto_vfr_skip: int
    auto_vfr_ref: int
    enable_resize: bool
    resize_width: int
    resize_height: int
    enable_temporal_nr: bool
    enable_deband: bool
    enable_edge_level: bool
    # extension_data: ? どうするか考える
