class StringValueObject:
    def __init__(self, value: str):
        self.value = value

    def to_string(self) -> str:
        return self.value
