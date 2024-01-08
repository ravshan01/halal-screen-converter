from abc import ABC, abstractmethod


class IConverterService(ABC):
    """Detect and blur persons on image"""

    @abstractmethod
    def convert(self, image: bytes) -> bytes:
        pass
