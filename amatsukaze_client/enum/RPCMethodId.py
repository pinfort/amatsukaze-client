from enum import Enum, unique

@unique
class RPCMethodId(Enum):
        SET_PROFILE = 100
        SET_AUTO_SELECT = 101
        ADD_QUEUE = 102
        CHANGE_ITEM = 103
        PAUSE_ENCODE = 104
        CANCEL_ADD_QUEUE = 105
        CANCEL_SLEEP = 106
        SET_COMMON_DATA = 107
        SET_SERVICE_SETTING = 108
        ADD_DRCS_MAP = 109
        END_SERVER = 110
        REQUEST = 111
        REQUEST_LOG_FILE = 112
        REQUEST_LOGO_DATA = 113
        REQUEST_DRCS_IMAGES = 114

        ON_UI_DATA = 200
        ON_CONSOLE_UPDATE = 201
        ON_ENCODE_STATE = 202
        ON_LOG_FILE = 203
        ON_COMMON_DATA = 204
        ON_PROFILE = 205
        ON_AUTO_SELECT = 206
        ON_SERVICE_SETTING = 207
        ON_LOGO_DATA = 208
        ON_DRCS_DATA = 209
        ON_ADD_RESULT = 210
        ON_OPERATION_RESULT = 211

        ADD_TAG = 300
        SET_OUT_DIR = 301
        SET_PRIORITY = 302
        GET_OUT_FILES = 303
        CANCEL_ITEM = 304
