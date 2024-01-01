from dataclasses import dataclass
from detection.enums.type import DetectionType


@dataclass
class DetectionPart:
    name: DetectionType
    score: float
    coords: list[int]  # x1, y1, x2 and y2 coordinates
