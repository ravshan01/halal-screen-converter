from abc import ABC, abstractmethod

from PIL import Image


class IConverterService(ABC):
    """Detect and blur persons on image"""

    @abstractmethod
    def convert(self, image: Image) -> Image:
        pass
