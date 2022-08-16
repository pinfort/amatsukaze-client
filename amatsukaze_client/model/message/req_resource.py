from dataclasses import dataclass


@dataclass
class ReqResource():
    cpu: int
    hdd: int
    gpu: int

    def canonical(self) -> int:
        return (self.cpu << 16) + (self.hdd << 8) + self.gpu

def from_canonical(c: int) -> ReqResource:
    return ReqResource(
        cpu=(c >> 16) & 0xFF,
        hdd=(c >> 8) & 0xFF,
        gpu=c & 0xFF,
    )
