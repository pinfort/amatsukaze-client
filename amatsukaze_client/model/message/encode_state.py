from dataclasses import dataclass

from amatsukaze_client.enum.message.resource_phase import ResourcePhase
from amatsukaze_client.model.message.resource import Resource

@dataclass
class EncodeState():
    console_id: int
    phase: ResourcePhase
    resource: Resource
