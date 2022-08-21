from ipaddress import IPv4Address

from amatsukaze_client.component.amatsukaze_communicator import AmatsukazeCommunicator
from amatsukaze_client.component.tcp_connection import TcpConnection
from amatsukaze_client.model.rpc.message import AmatsukazeRPCMessage
from amatsukaze_client.enum.rpc.message_type_id import AmatsukazeRPCMessageTypeId
from amatsukaze_client.model.rpc.message_container import AmatsukazeRPCMessageContainer


class TcpConnection4Test(TcpConnection):
    def __init__(self) -> None:
        pass

    def connect(self, ip: IPv4Address, port: int) -> None:
        pass

    def send(self, messsage: bytes) -> int:
        return len(messsage)

    def recv(self, length: int) -> bytes:
        return length.to_bytes(4, byteorder="little")

    def __del__(self) -> None:
        pass


tcp_connection = TcpConnection4Test()


def test_send_success():
    communicator = AmatsukazeCommunicator(tcp_connection)
    actual: int = communicator.send(
        AmatsukazeRPCMessageContainer(
            message_type_id=AmatsukazeRPCMessageTypeId.ADD_DRCS_MAP,
            length=100,
            messages=[AmatsukazeRPCMessage(length=20, message_body=b"bytes for test")],
        )
    )
    assert actual == 24
