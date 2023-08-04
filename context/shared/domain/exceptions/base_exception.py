from fastapi import HTTPException


class BaseException(HTTPException):
    def __init__(self, status_code: int, message: str, *args):
        super(BaseException, self).__init__(status_code, detail=message, *args)
