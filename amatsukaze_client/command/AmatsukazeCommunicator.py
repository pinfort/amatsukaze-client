from typing import Iterator
from amatsukaze_client.component.TcpConnection import TcpConnection
from amatsukaze_client.enum.AmatsukazeRPCMessageTypeId import AmatsukazeRPCMessageTypeId
from amatsukaze_client.model.AmatsukazeRPCMessage import AmatsukazeRPCMessage
from amatsukaze_client.model.AmatsukazeRPCMessageContainer import AmatsukazeRPCMessageContainer

class AmatsukazeCommunicator():
    __tcpConnection: TcpConnection

    def __init__(self, tcpConnection: TcpConnection):
        self.__tcpConnection = tcpConnection

    def send(self, containeredMessage: AmatsukazeRPCMessageContainer) -> int:
        self.__tcpConnection.send(containeredMessage.toBytes())

    def recv(self) -> AmatsukazeRPCMessageContainer:
        """
            TCPソケットからデータを取得。メッセージコンテナ一つ分のメッセージを取得します。
        """
        messagesTypeId: int = int.from_bytes(self.__tcpConnection.recv(2), byteorder='little')
        messagesLength: int = int.from_bytes(self.__tcpConnection.recv(4), byteorder='little')
        messages: bytes = self.__tcpConnection.recv(messagesLength)
        return AmatsukazeRPCMessageContainer(
            messageTypeId=AmatsukazeRPCMessageTypeId(messagesTypeId),
            length=messagesLength,
            messages=list(self.__getMessagesBytes(messages)),
        )

    def __getMessagesBytes(messages: bytes) -> Iterator[AmatsukazeRPCMessage]:
        """
            メッセージコンテナの中のメッセージを受け取ってGeneratorで返します
        """
        offset: int = 0
        while offset < len(messages):
            messageLength: int = int.from_bytes(messages[offset:offset + 4], byteorder='little')
            offset: int = offset + 4
            message: bytes = messages[offset:offset+messageLength]
            offset: int = offset + messageLength
            yield AmatsukazeRPCMessage(
                length=messageLength,
                messageBody=message,
            )
