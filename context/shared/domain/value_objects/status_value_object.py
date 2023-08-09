from abc import ABC, abstractmethod
from context.shared.domain.value_objects.string_value_object import StringValueObject


class StatusValueObject(StringValueObject, ABC):

    def __init__(self, value: str):
        super().__init__(value)

    @abstractmethod
    def _validate_status(self, value: str):
        pass
