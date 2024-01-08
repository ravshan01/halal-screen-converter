from abc import ABC, abstractmethod


class IConverterService(ABC):
    """Detect and blur persons in images and videos."""

    @abstractmethod
    def convert_image(self, image: bytes) -> bytes:
        pass

    @abstractmethod
    def convert_video(self, video: bytes) -> bytes:
        pass
