from PIL import Image, ImageDraw

from .detection import detection_service
from detection.enums.type import DetectionType
from mock.images import room, person, street


class TestDetectionService:
    def test_detect(self):
        for m in [room, person, street]:
            image = Image.open(m.resource.path)
            detections = detection_service.detect(image, min_percentage_probability=30)

            # draw = ImageDraw.Draw(image)
            # for detection in detections:
            #     draw.rectangle(detection.coords, outline="red", width=3)
            # image.show()

            assert len(detections) == m.resource.detections[DetectionType.Person]
