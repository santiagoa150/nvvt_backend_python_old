from fastapi import HTTPException


class BadRequestException(HTTPException):
    def __init__(self, *args):
        super().__init__(status_code=400, detail={"message": "BAD_REQUEST"}, *args)
