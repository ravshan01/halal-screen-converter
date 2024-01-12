import io
import tempfile

from PIL import Image
import cv2
import numpy as np

from detection.services.detection import detection_service
from images.services.images import images_service
from .IConverterService import IConverterService


class ConverterService(IConverterService):
    detection_service = detection_service
    images_service = images_service

    def convert_image(self, image: bytes) -> bytes:
        blured_image = self.__detect_and_blur(Image.open(io.BytesIO(image)))

        byte_io = io.BytesIO()
        blured_image.save(byte_io, format="PNG")  # TODO: get format from image
        return byte_io.getvalue()

    def convert_video(self, video: bytes) -> bytes:
        temp_file = tempfile.NamedTemporaryFile(suffix=".mp4", delete=False)
        temp_file.write(video)
        video_path = temp_file.name

        # Создание объекта VideoCapture и открытие временного файла
        capture = cv2.VideoCapture()
        capture.open(video_path)

        fps = capture.get(cv2.CAP_PROP_FPS)
        width = int(capture.get(cv2.CAP_PROP_FRAME_WIDTH))
        height = int(capture.get(cv2.CAP_PROP_FRAME_HEIGHT))

        output = cv2.VideoWriter(
            "output.mp4",
            cv2.VideoWriter_fourcc(*"mp4v"),
            fps,
            (width, height),
        )

        while capture.isOpened():
            ret, frame = capture.read()
            if not ret:
                break

            blured_frame = self.__detect_and_blur(Image.fromarray(frame))
            output.write(np.array(blured_frame))

        output.release()
        capture.release()
        temp_file.close()

    def __detect_and_blur(self, image: Image) -> Image:
        detections = self.detection_service.detect(image)
        boxes = list(
            map(
                lambda det: tuple(map(lambda coord: int(coord), det.coords)), detections
            )
        )
        blured_image = self.images_service.blur_boxes(
            image,
            boxes=boxes,
            percentage=50,
        )

        return blured_image


converter_service = ConverterService()
