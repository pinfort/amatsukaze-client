from dataclasses import dataclass


@dataclass
class ServerInfo:
    host_name: str
    mac_address: bytes
    version: str
