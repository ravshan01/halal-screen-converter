from typing import Protocol


class DetectionPartProtocol(Protocol):
    name: str
    score: float
    box_points: list[int]  # x1, y1, x2 and y2 coordinates
