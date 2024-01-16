from abc import ABC, abstractmethod


class IConverterService(ABC):
    """Detect and blur persons in images and videos."""

    @abstractmethod
    def convert_image(self, image: bytes, blur_percentage: int = 50) -> bytes:
        pass

    @abstractmethod
    def convert_video(self, video: bytes, blur_percentage: int = 50) -> bytes:
        pass
