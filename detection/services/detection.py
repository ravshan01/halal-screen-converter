from pathlib import PurePath

import torch
from ultralytics import YOLO
from PIL import Image

from core.config import config
from settings import ROOT_DIR
from detection.dataclasses.part import DetectionPart
from detection.enums.type import DetectionType
from detection.services.IDetectionService import IDetectionService


class DetectionService(IDetectionService):
    person_type = 0

    def __init__(self):
        if torch.cuda.is_available():
            torch.cuda.set_device(0)

        self.model = YOLO(str(PurePath(ROOT_DIR, config.weights_path)))

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
