from dataclasses import dataclass
from typing import List

from amatsukaze_client.enum.AmatsukazeRPCMessageTypeId import AmatsukazeRPCMessageTypeId
from amatsukaze_client.model.AmatsukazeRPCMessage import AmatsukazeRPCMessage


@dataclass
class AmatsukazeRPCMessageContainer():
    messageTypeId: AmatsukazeRPCMessageTypeId
    length: int
    messages: List[AmatsukazeRPCMessage]

    def toBytes(self) -> bytes:
        """
            メッセージコンテナは以下の構造である。
            -----------------------------------
            | 2bytes | 4bytes | N bytes       |
            | typeId | length | messageBodies |
            -----------------------------------
        """
        return self.messageTypeId.value.to_bytes(2, byteorder='little') \
         + self.length.to_bytes(4, byteorder='little') \
         + self.__messagesToBytes()

    def __messagesToBytes(self) -> bytes:
        messageBytes = b''
        for message in self.messages:
            messageBytes = messageBytes + message.toBytes()
        return messageBytes
