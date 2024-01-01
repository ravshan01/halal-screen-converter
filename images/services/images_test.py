import numpy
from PIL import Image

from .images import images_service
from mock.images import room


class TestImageService:
    def test_blur(self):
        image = Image.open(room.resource.path)
        image_np = numpy.array(image)

        blured_image = images_service.blur(image, percentage=50)
        blured_image_np = numpy.array(blured_image)

        assert not numpy.array_equal(image_np, blured_image_np)
