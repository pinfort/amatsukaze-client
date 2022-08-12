from dataclasses import dataclass

@dataclass
class AmatsukazeRPCMessage():
    length: int
    message_body: bytes

    def to_bytes(self) -> bytes:
        """
        一つのメッセージは、以下のように、4bytes + bodyの形式である。
        ----------------------------
        | 4bytes | {length} bytes  |
        | length | message body    |
        ----------------------------
        """
        self.length.to_bytes(4, byteorder='little') + self.message_body

def from_bytes(message_body: bytes) -> AmatsukazeRPCMessage:
    return AmatsukazeRPCMessage(length=len(message_body), message_body=message_body)
