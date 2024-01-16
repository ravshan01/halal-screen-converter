from PIL import Image, ImageFilter

from images.services.IImagesService import IImagesService
from images.errors.invalid_percentage import InvalidPercentageError


class ImagesService(IImagesService):
    def blur(self, image: Image, percentage: int = 50) -> Image:
        self.__raise_invalid_percentage_error_if_need(percentage)

        # I haven't come up with anything else to calculate the radius
        return image.filter(
            ImageFilter.GaussianBlur(
                (
                    int((image.width * (percentage / 700))),
                    int((image.height * (percentage / 700))),
                )
            )
        )

    def blur_boxes(
        self, image: Image, boxes: list[tuple[int, int, int, int]], percentage: int = 50
    ) -> Image:
        self.__raise_invalid_percentage_error_if_need(percentage)

        image_copy = image.copy()
        for box in boxes:
            image_part = image.crop(box)
            blured_part = self.blur(image_part, percentage)
            image_copy.paste(blured_part, box)

        return image_copy

    def __raise_invalid_percentage_error_if_need(self, percentage: int):
        if percentage < 0 or percentage > 100:
            raise InvalidPercentageError(percentage)


images_service = ImagesService()
