from amatsukaze_client.model.rpc.message import (
    AmatsukazeRPCMessage,
    from_bytes,
    from_messages_bytes,
)


def test_from_bytes_success():
    actual: AmatsukazeRPCMessage = from_bytes(b"test bytes")

    expected = AmatsukazeRPCMessage(
        length=10,
        message_body=b"test bytes",
    )

    assert actual == expected


def test_from_messages_bytes_success():
    actual = list(
        from_messages_bytes(b"\x0a\x00\x00\x00test bytes\x0c\x00\x00\x00second bytes")
    )

    expected = [
        AmatsukazeRPCMessage(
            length=10,
            message_body=b"test bytes",
        ),
        AmatsukazeRPCMessage(
            length=12,
            message_body=b"second bytes",
        ),
    ]

    assert actual == expected
