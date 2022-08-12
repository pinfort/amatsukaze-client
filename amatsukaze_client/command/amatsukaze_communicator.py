from typing import Iterator
from amatsukaze_client.component.tcp_connection import TcpConnection
from amatsukaze_client.enum.rpc.message_type_id import AmatsukazeRPCMessageTypeId
from amatsukaze_client.model.rpc.message import AmatsukazeRPCMessage
from amatsukaze_client.model.rpc.message_container import AmatsukazeRPCMessageContainer

class AmatsukazeCommunicator():
    __tcp_connection: TcpConnection

    def __init__(self, tcp_connection: TcpConnection):
        self.__tcp_connection = tcp_connection

    def send(self, containered_message: AmatsukazeRPCMessageContainer) -> int:
        self.__tcp_connection.send(containered_message.to_bytes())

    def recv(self) -> AmatsukazeRPCMessageContainer:
        """
            TCPソケットからデータを取得。メッセージコンテナ一つ分のメッセージを取得します。
        """
        messages_type_id: int = int.from_bytes(self.__tcp_connection.recv(2), byteorder='little')
        messages_length: int = int.from_bytes(self.__tcp_connection.recv(4), byteorder='little')
        messages: bytes = self.__tcp_connection.recv(messages_length)
        return AmatsukazeRPCMessageContainer(
            message_type_id=AmatsukazeRPCMessageTypeId(messages_type_id),
            length=messages_length,
            messages=list(self.__get_messages_bytes(messages)),
        )

    def __get_messages_bytes(messages: bytes) -> Iterator[AmatsukazeRPCMessage]:
        """
            メッセージコンテナの中のメッセージを受け取ってGeneratorで返します
        """
        offset: int = 0
        while offset < len(messages):
            message_length: int = int.from_bytes(messages[offset:offset + 4], byteorder='little')
            offset: int = offset + 4
            message: bytes = messages[offset:offset+message_length]
            offset: int = offset + message_length
            yield AmatsukazeRPCMessage(
                length=message_length,
                message_body=message,
            )
