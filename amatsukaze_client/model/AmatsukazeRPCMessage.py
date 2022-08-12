from dataclasses import dataclass

@dataclass
class AmatsukazeRPCMessage():
    length: int
    messageBody: bytes

    def toBytes(self) -> bytes:
        """
        一つのメッセージは、以下のように、4bytes + bodyの形式である。
        ----------------------------
        | 4bytes | {length} bytes  |
        | length | message body    |
        ----------------------------
        """
        self.length.to_bytes(4, byteorder='little') + self.messageBody

def fromBytes(messageBody: bytes) -> AmatsukazeRPCMessage:
    return AmatsukazeRPCMessage(length=len(messageBody), messageBody=messageBody)
