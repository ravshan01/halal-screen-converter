import numpy
from PIL import Image

from .images import images_service
from mock.images import room


class TestImageService:
    def test_blur(self):
        image = Image.open(room.resource.path)
        blured_image = images_service.blur(image, percentage=50)

        assert not numpy.array_equal(numpy.array(image), numpy.array(blured_image))

    def test_blur_boxes(self):
        image = Image.open(room.resource.path)
        boxes = [
            (0, 0, 200, 200),
            (400, 0, 600, 200),
            (200, 200, 400, 400),
            (500, 400, 900, 700),
        ]
        blured_image = images_service.blur_boxes(
            image,
            boxes,
            percentage=50,
        )

        for box in boxes:
            image_part = image.crop(box)
            blured_part = blured_image.crop(box)

            assert not numpy.array_equal(
                numpy.array(image_part), numpy.array(blured_part)
            )
