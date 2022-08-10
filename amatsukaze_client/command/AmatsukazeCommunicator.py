from pyexpat.errors import messages
from typing import Generator, List, Tuple
from amatsukaze_client.component.TcpConnection import TcpConnection

class AmatsukazeCommunicator():
    __tcpConnection: TcpConnection

    def __init__(self, tcpConnection: TcpConnection):
        self.__tcpConnection = tcpConnection

    def send(self, message: bytes) -> int:
        length: int = len(bytes)
        lengthByBytes: bytes = length.to_bytes(4, byteorder='little')
        self.__tcpConnection.send(lengthByBytes + message)

    def recv(self) -> Tuple[int, List[bytes]]:
        messagesTypeId: int = int.from_bytes(self.__tcpConnection.recv(2), byteorder='little')
        messagesLength: int = int.from_bytes(self.__tcpConnection.recv(4), byteorder='little')
        messages: bytes = self.__tcpConnection.recv(messagesLength)
        return (messagesTypeId, list(self.__getMessagesBytes(messages)))

    def __getMessagesBytes(messages: bytes) -> Generator[bytes]:
        offset: int = 0
        while offset < len(messages):
            messageLength: int = int.from_bytes(messages[offset:offset + 4], byteorder='little')
            offset: int = offset + 4
            message: bytes = messages[offset:offset+messageLength]
            offset: int = offset + messageLength
            yield message
