from ultralytics import YOLO

from detection.dataclasses.part import DetectionPart
from detection.enums.type import DetectionType
from detection.services.IDetectionService import IDetectionService
from PIL import Image


class DetectionService(IDetectionService):
    person_type = 0

    def __init__(self):
        self.model = YOLO("yolov8s.pt")

    def detect(self, image: Image) -> list[DetectionPart]:
        detects = self.model.predict(image, save=True)[0]

        persons_indexes = []
        for i, val in enumerate(detects.boxes.cls):
            if val == self.person_type:
                persons_indexes.append(i)

        return list(
            map(
                lambda i: DetectionPart(
                    name=DetectionType.Person,
                    score=detects.boxes.conf[i].item(),
                    coords=tuple(detects.boxes.xyxy[i].tolist()),
                ),
                persons_indexes,
            )
        )


detection_service = DetectionService()
