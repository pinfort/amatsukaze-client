from typing import Iterator

from amatsukaze_client.component.tcp_connection import TcpConnection
from amatsukaze_client.model.rpc.message_container import (
    AmatsukazeRPCMessageContainer,
    from_messages_bytes,
)


class AmatsukazeCommunicator:
    __tcp_connection: TcpConnection

    def __init__(self, tcp_connection: TcpConnection):
        self.__tcp_connection = tcp_connection

    def send(self, containered_message: AmatsukazeRPCMessageContainer) -> int:
        return self.__tcp_connection.send(containered_message.to_bytes())

    def recv(self) -> AmatsukazeRPCMessageContainer:
        """
        TCPソケットからデータを取得。メッセージコンテナ一つ分のメッセージを取得します。
        """
        messages_type_id: int = int.from_bytes(
            self.__tcp_connection.recv(2), byteorder="little"
        )
        messages_length: int = int.from_bytes(
            self.__tcp_connection.recv(4), byteorder="little"
        )
        messages: bytes = self.__tcp_connection.recv(messages_length)
        return from_messages_bytes(
            message_type_id=messages_type_id, length=messages_length, messages=messages
        )
