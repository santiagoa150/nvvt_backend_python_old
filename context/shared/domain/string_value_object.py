from .exception.bad_request_exception import BadRequestException


class StringValueObject:
    value: str

    def __init__(self, value: str):
        if type(value) is not str:
            raise BadRequestException()
        self.value = value
