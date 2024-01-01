from abc import ABC, abstractmethod
from PIL import Image
from detection.protocols.part import DetectionPartProtocol


class IDetectionService(ABC):
    """Person detection service interface"""

    @abstractmethod
    def detect(
        self,
        image: Image,
        min_percentage_probability: int = 50,
    ) -> list[DetectionPartProtocol]:
        pass
