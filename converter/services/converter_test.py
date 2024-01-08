import io

import numpy
from PIL import Image

from .converter import converter_service
from mock.images import room, street, traffic


class TestConverterService:
    def test_convert(self):
        for m in [room, street, traffic]:
            with open(m.resource.path, "rb") as image_file:
                image = image_file.read()
                image_pil = Image.open(io.BytesIO(image))
                converted_image = converter_service.convert(image)
                converted_image_pil = Image.open(io.BytesIO(converted_image))

                detections = converter_service.detection_service.detect(image_pil)
                for detection in detections:
                    image_part = image_pil.crop(detection.coords)
                    converted_image_part = converted_image_pil.crop(detection.coords)

                    assert not numpy.array_equal(
                        numpy.array(image_part), numpy.array(converted_image_part)
                    )
