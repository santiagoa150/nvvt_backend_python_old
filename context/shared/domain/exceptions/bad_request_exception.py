from fastapi import status

from .base_exception import BaseException
from context.shared.domain.constants.error_constants import ErrorConstants


class BadRequestException(BaseException):
    def __init__(self, *args):
        super().__init__(status_code=status.HTTP_400_BAD_REQUEST, message=ErrorConstants.BAD_REQUEST_ERROR, *args)
