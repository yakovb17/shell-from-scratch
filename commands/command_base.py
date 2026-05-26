from abc import ABC, abstractmethod


class Command(ABC):
    def __init__(self, *args, **kwargs) -> None: ...

    @abstractmethod
    def execute(self, args) -> None:
        raise NotImplementedError
