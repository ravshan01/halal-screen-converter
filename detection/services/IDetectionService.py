from abc import ABC, abstractmethod
from PIL import Image
from detection.dataclasses.part import DetectionPart


class IDetectionService(ABC):
    """Person detection service interface"""

    @abstractmethod
    def detect(self, images: list[Image]) -> list[list[DetectionPart]]:
        pass
