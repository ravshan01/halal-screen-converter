from PIL import Image, ImageFilter

from images.services.IImagesService import IImagesService


class ImagesService(IImagesService):
    def blur(self, image: Image, percentage: int = 50) -> Image:
        img_copy = image.copy()
        img_copy.filter(ImageFilter.GaussianBlur(percentage))
        return img_copy

    def blur_boxes(
        self, image: Image, boxes: list[list[int, int, int, int]], percentage: int = 50
    ) -> Image:
        image_copy = image.copy()
        for box in boxes:
            image_part = image.crop(box)
            blured_part = self.blur(image_part, percentage)
            image_copy.paste(blured_part, box)

        return image_copy

    def rgba_2_rgb(self, image: Image) -> Image:
        return image.convert("RGB")


images_service = ImagesService()
