from dataclasses import dataclass


@dataclass
class MakeScriptData:
    profile: str
    out_dir: str
    nas_dir: str
    is_nas_enabled: bool
    is_wake_on_lan: bool
    move_after: bool
    clear_encoded: bool
    with_related: bool
    is_direct: bool
    priority: int
    add_queue_bat: str
