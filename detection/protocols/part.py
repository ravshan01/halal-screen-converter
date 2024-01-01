from typing import Protocol
from detection.enums.type import DetectionType


class DetectionPartProtocol(Protocol):
    name: DetectionType
    score: float
    box_points: list[int]  # x1, y1, x2 and y2 coordinates
