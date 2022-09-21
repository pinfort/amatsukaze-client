from amatsukaze_client.enum.rpc.message_type_id import AmatsukazeRPCMessageTypeId
from amatsukaze_client.model.rpc.message import AmatsukazeRPCMessage
from amatsukaze_client.model.rpc.message_container import (
    AmatsukazeRPCMessageContainer,
    from_messages_bytes,
)


def test_from_messages_bytes():
    actual: AmatsukazeRPCMessageContainer = from_messages_bytes(
        message_type_id=AmatsukazeRPCMessageTypeId.ADD_DRCS_MAP,
        length=100,
        messages_bytes=b"\x0a\x00\x00\x00test bytes\x0c\x00\x00\x00second bytes",
    )

    expected = AmatsukazeRPCMessageContainer(
        message_type_id=AmatsukazeRPCMessageTypeId.ADD_DRCS_MAP,
        length=100,
        messages=[
            AmatsukazeRPCMessage(
                length=10,
                message_body=b"test bytes",
            ),
            AmatsukazeRPCMessage(
                length=12,
                message_body=b"second bytes",
            ),
        ],
    )

    assert actual == expected
