from dataclasses import dataclass

from .req_resource import ReqResource


@dataclass
class Resource():
    req_resource: ReqResource
    gpu_index: int
    encoder_index: int
