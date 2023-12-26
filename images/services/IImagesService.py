from abc import ABC, abstractmethod
from PIL.Image import Image
from numpy import ndarray


class IImagesService(ABC):
    @abstractmethod
    def blur(self, image: Image, percentage: int = 50) -> Image:
        pass

    @abstractmethod
    def blur_boxes(
        self, image: Image, boxes: list[list[int, int, int, int]], percentage: int = 50
    ) -> Image:
        """
        :param image:
        :param boxes: list [x1, y1, x2, y2]
        :param percentage:
        :return image with blured boxes:
        """
        pass

    @abstractmethod
    def remove_opacity_data_from_numpy_array(self, image: Image | ndarray) -> ndarray:
        """
        numpy array shape (height, width, 4) -> (height, width, 3)
        """
        pass