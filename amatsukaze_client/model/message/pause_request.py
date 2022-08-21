from dataclasses import dataclass


@dataclass
class PauseRequest:
    # true: キュー停止, false: エンコーダ停止
    is_queue: bool
    # 停止するエンコーダ -1の場合は全エンコーダ
    index: int
    # 停止か稼働か
    pause: bool
