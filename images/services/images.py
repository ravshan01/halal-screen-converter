from PIL import Image, ImageFilter

from images.services.IImagesService import IImagesService


class ImagesService(IImagesService):
    def blur(self, image: Image, percentage: int = 50) -> Image:
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
        image_copy = image.copy()
        for box in boxes:
            image_part = image.crop(box)
            blured_part = self.blur(image_part, percentage)
            image_copy.paste(blured_part, box)

        return image_copy


images_service = ImagesService()
