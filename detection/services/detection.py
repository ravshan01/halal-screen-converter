from ultralytics import YOLO

from detection.dataclasses.part import DetectionPart
from detection.enums.type import DetectionType
from detection.services.IDetectionService import IDetectionService
from PIL import Image


class DetectionService(IDetectionService):
    person_type = 0

    def __init__(self):
        self.model = YOLO("yolov8s.pt")

    def detect(self, images: list[Image]) -> list[list[DetectionPart]]:
        results = self.model.predict(images)
        return list(map(self.__generate_detections, results))

    def __generate_detections(self, result) -> list[DetectionPart]:
        persons_indexes = []

        for i, val in enumerate(result.boxes.cls):
            if val == self.person_type:
                persons_indexes.append(i)

        return list(
            map(
                lambda i: DetectionPart(
                    name=DetectionType.Person,
                    score=result.boxes.conf[i].item(),
                    coords=tuple(result.boxes.xyxy[i].tolist()),
                ),
                persons_indexes,
            )
        )


detection_service = DetectionService()
