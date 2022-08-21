from amatsukaze_client.model.rpc.message import AmatsukazeRPCMessage
from amatsukaze_client.enum.rpc.message_type_id import AmatsukazeRPCMessageTypeId
from amatsukaze_client.model.rpc.message_container import AmatsukazeRPCMessageContainer


def test_to_bytes_success():
    container = AmatsukazeRPCMessageContainer(
        message_type_id=AmatsukazeRPCMessageTypeId.ADD_DRCS_MAP,
        length=200,
        messages=[
            AmatsukazeRPCMessage(
                length=100,
                message_body=b"test bytes",
            ),
        ],
    )

    actual: bytes = container.to_bytes()

    expected: bytes = b"\x6d\x00\xc8\x00\x00\x00\x64\x00\x00\x00test bytes"

    assert actual == expected


def test_to_bytes_multimessage_success():
    container = AmatsukazeRPCMessageContainer(
        message_type_id=AmatsukazeRPCMessageTypeId.ADD_DRCS_MAP,
        length=200,
        messages=[
            AmatsukazeRPCMessage(
                length=100,
                message_body=b"test bytes",
            ),
            AmatsukazeRPCMessage(
                length=26383,
                message_body=b"second bytes",
            ),
        ],
    )

    actual: bytes = container.to_bytes()

    expected: bytes = b"\x6d\x00\xc8\x00\x00\x00\x64\x00\x00\x00test bytes\x0f\x67\x00\x00second bytes"

    assert actual == expected
