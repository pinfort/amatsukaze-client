from amatsukaze_client.model.rpc.message import AmatsukazeRPCMessage


def test_to_bytes_success():
    message = AmatsukazeRPCMessage(
        length=100,
        message_body=b'test bytes',
    )

    actual: bytes = message.to_bytes()

    expected: bytes = b'\x64\x00\x00\x00test bytes'

    assert actual == expected
