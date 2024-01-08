from abc import ABC, abstractmethod


class IConverterService(ABC):
    """Detect and blur persons on image"""

    @abstractmethod
    def convert_image(self, image: bytes) -> bytes:
        pass
