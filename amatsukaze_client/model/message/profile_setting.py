from dataclasses import dataclass
from datetime import datetime
from typing import List

from amatsukaze_client.enum.message.audio_encoder_type import AudioEncoderType
from amatsukaze_client.enum.message.decoder_type import DecoderType
from amatsukaze_client.enum.message.encoder_type import EncoderType
from amatsukaze_client.enum.message.filter_option import FilterOption
from amatsukaze_client.enum.message.format_type import FormatType
from amatsukaze_client.model.message.bitrate_setting import BitrateSetting
from amatsukaze_client.model.message.filter_setting import FilterSetting
from amatsukaze_client.model.message.req_resource import ReqResource


@dataclass
class ProfileSetting:
    name: str
    last_update: datetime
    encoder_type: EncoderType
    x264_option: str
    x265_option: str
    qsv_enc_option: str
    nvenc_option: str
    vceenc_option: str
    svtav1_option: str

    mpeg2_decoder: DecoderType
    h264_decoder: DecoderType
    output_format: FormatType

    filter_path: str
    post_filter_path: str

    two_pass: bool
    split_sub: bool
    output_mask: int
    auto_buffer: bool
    bitrate: BitrateSetting
    bitrate_cm: float

    jls_command_file: str
    jls_option: str
    chapter_exe_option: str
    enable_jls_option: bool
    disable_chapter: bool
    disable_subs: bool
    ignore_no_drcs_map: bool
    loose_logo_detection: bool
    ignore_no_logo: bool
    no_delogo: bool
    system_avi_synsth_plugin: bool
    disable_hash_check: bool
    enable_nico_jk: bool
    ignore_nico_jk_error: bool
    nico_jk_18: bool
    nico_jk_log: bool
    nico_jk_formats: List[bool]
    move_ecdb_files: bool
    no_remove_tmp: bool
    disable_log_file: bool

    enable_max_fade_length: bool
    max_fade_length: int

    enable_rename: bool
    rename_format: str
    enable_gunre_folder: bool
    req_resources: List[ReqResource]

    enable_pmt_cut: bool
    pmt_cut_head_rate: float
    pmt_cut_tail_rate: float

    ignore_encode_affinity: bool

    pre_batch_file: str
    post_batch_file: str

    filter_option: FilterOption
    filter_setting: FilterSetting
    num_encode_buffer_frames: int
    additional_erace_logo: str
    enable_audio_encode: bool
    audio_encoder_type: AudioEncoderType
    nero_aac_option: str
    qaac_option: str
    fdkaac_option: str
    enable_audio_bitrate: bool
    audio_bitrate_in_kbps: int

    # extension_date: ? どうするか考える

    @property
    def nico_jk_format_mask(self) -> int:
        mask: int = 0
        for i in reversed(range(0, len(self.nico_jk_formats) - 1)):
            mask = mask << 1
            mask = mask | (1 if self.nico_jk_formats else 0)
        return mask
