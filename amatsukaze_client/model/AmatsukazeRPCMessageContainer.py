from dataclasses import dataclass
from typing import List

from amatsukaze_client.enum.AmatsukazeRPCMessageTypeId import AmatsukazeRPCMessageTypeId
from amatsukaze_client.model.AmatsukazeRPCMessage import AmatsukazeRPCMessage


@dataclass
class AmatsukazeRPCMessageContainer():
    message_type_id: AmatsukazeRPCMessageTypeId
    length: int
    messages: List[AmatsukazeRPCMessage]

    def toBytes(self) -> bytes:
        """
            メッセージコンテナは以下の構造である。
            -----------------------------------
            | 2bytes | 4bytes | N bytes        |
            | typeId | length | message bodies |
            -----------------------------------
        """
        return self.message_type_id.value.to_bytes(2, byteorder='little') \
         + self.length.to_bytes(4, byteorder='little') \
         + self.__messagesToBytes()

    def __messagesToBytes(self) -> bytes:
        message_bytes: bytes = b''
        for message in self.messages:
            message_bytes = message_bytes + message.toBytes()
        return message_bytes
