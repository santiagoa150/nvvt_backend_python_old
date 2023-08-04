from uuid import uuid4
from context.shared.domain.string_value_object import StringValueObject


class IdValueObject(StringValueObject):

    @staticmethod
    def generate() -> str:
        return str(uuid4())
