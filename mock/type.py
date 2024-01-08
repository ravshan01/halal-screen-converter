from dataclasses import dataclass
from enum import Enum

from detection.enums.type import DetectionType


class MockResourceEnum(Enum):
    Image = "image"
    Video = "video"


@dataclass
class MockResource:
    type: MockResourceEnum
    path: str
    detections: dict[DetectionType, int] | None = None
