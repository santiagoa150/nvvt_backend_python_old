class StringValueObject:
    def __init__(self, value: str):
        self.__value = value

    def to_string(self) -> str:
        return self.__value
