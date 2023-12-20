from typing import Protocol


class DetectionPartProtocol(Protocol):
    coords: list[int]
    class_name: str
    score: float
