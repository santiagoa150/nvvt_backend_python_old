from abc import ABC, abstractmethod


class DomainRoot(ABC):

    @abstractmethod
    def to_primitives(self):
        pass
