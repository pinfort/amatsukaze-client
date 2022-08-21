from enum import IntFlag, unique


@unique
class ServerRequest(IntFlag):
    SETTING = 1
    QUEUE = 1 << 1
    LOG = 1 << 2
    CHECK_LOG = 1 << 3
    CONSOLE = 1 << 4
    STATE = 1 << 5
    FREE_SPACE = 1 << 6
    SERVICE_SETTING = 1 << 7
