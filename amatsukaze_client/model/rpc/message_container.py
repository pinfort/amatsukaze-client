from dataclasses import dataclass
from typing import List

from amatsukaze_client.enum.rpc.message_type_id import AmatsukazeRPCMessageTypeId
from amatsukaze_client.model.rpc.message import AmatsukazeRPCMessage


@dataclass
class AmatsukazeRPCMessageContainer():
    message_type_id: AmatsukazeRPCMessageTypeId
    length: int
    messages: List[AmatsukazeRPCMessage]

    def to_bytes(self) -> bytes:
        """
            メッセージコンテナは以下の構造である。
            ||||
            |--------|--------|----------------|
            | 2bytes | 4bytes | N bytes        |
            | typeId | length | message bodies |
            -----------------------------------
        """
        return self.message_type_id.value.to_bytes(2, byteorder='little') \
         + self.length.to_bytes(4, byteorder='little') \
         + self.__messages_to_bytes()

    def __messages_to_bytes(self) -> bytes:
        message_bytes: bytes = b''
        for message in self.messages:
            message_bytes = message_bytes + message.to_bytes()
        return message_bytes
