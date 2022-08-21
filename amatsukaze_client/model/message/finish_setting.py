from dataclasses import dataclass

from amatsukaze_client.enum.message.finish_action import FinishAction


@dataclass
class FinishSetting:
    action: FinishAction
    seconds: int
