from enum import Enum


class ErrorConstants(str, Enum):
    BAD_REQUEST_ERROR = 'BAD_REQUEST_ERROR',
    INTERNAL_SERVER_ERROR = 'INTERNAL_SERVER_ERROR',