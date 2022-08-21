from dataclasses import dataclass
from typing import Iterator, List


@dataclass
class AmatsukazeRPCMessage:
    length: int
    message_body: bytes

    def to_bytes(self) -> bytes:
        """
        一つのメッセージは、以下のように、4bytes + bodyの形式である。
        |||
        |--------|-----------------|
        | 4bytes | {length} bytes  |
        | length | message body    |
        ----------------------------
        """
        return self.length.to_bytes(4, byteorder="little") + self.message_body


def from_bytes(message_body: bytes) -> AmatsukazeRPCMessage:
    return AmatsukazeRPCMessage(length=len(message_body), message_body=message_body)


def from_messages_bytes(messages: bytes) -> Iterator[AmatsukazeRPCMessage]:
    """
    メッセージのバイト列（ヘッダー付き）を受け取ってIteratorで返します
    """
    offset: int = 0
    while offset < len(messages):
        message_length: int = int.from_bytes(
            messages[offset : offset + 4], byteorder="little"
        )
        offset: int = offset + 4
        message: bytes = messages[offset : offset + message_length]
        offset: int = offset + message_length
        yield AmatsukazeRPCMessage(
            length=message_length,
            message_body=message,
        )
