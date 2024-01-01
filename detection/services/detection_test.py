from PIL import Image

from detection.enums.type import DetectionType
from detection.services.detection import detection_service
from mock.images import room, person, street


class TestDetectionService:
    def test_detect(self):
        for m in [room, person, street]:
            image = Image.open(m.resource.path)
            detections = detection_service.detect(image, min_percentage_probability=30)

            print(len(detections))
            assert len(detections) == m.resource.detections[DetectionType.Person]
