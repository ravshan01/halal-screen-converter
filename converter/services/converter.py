import io
import os
import tempfile
from pathlib import PurePath

from PIL import Image
import cv2
import numpy as np

from .IConverterService import IConverterService
from detection.services.IDetectionService import IDetectionService
from images.services.IImagesService import IImagesService
from detection.services.detection import (
    detection_service as detection_service_realization,
)
from images.services.images import images_service as images_service_realization


class ConverterService(IConverterService):
    def __init__(
          self, detection_service: IDetectionService, images_service: IImagesService
    ):
        self.detection_service = detection_service
        self.images_service = images_service

    def convert_image(self, image: bytes, blur_percentage: int = 50) -> bytes:
        blured_image = self.__detect_and_blur(
            Image.open(io.BytesIO(image)), blur_percentage
        )

        byte_io = io.BytesIO()
        blured_image.save(byte_io, format="PNG")  # TODO: get format from image
        return byte_io.getvalue()

    def convert_video(self, video: bytes, blur_percentage: int = 50) -> bytes:
        temp_file = tempfile.NamedTemporaryFile(suffix=".mp4")
        temp_file.write(video)

        capture = cv2.VideoCapture()
        capture.open(temp_file.name)

        fps = capture.get(cv2.CAP_PROP_FPS)
        width = int(capture.get(cv2.CAP_PROP_FRAME_WIDTH))
        height = int(capture.get(cv2.CAP_PROP_FRAME_HEIGHT))

        new_file_name = PurePath(temp_file.name).name
        output = cv2.VideoWriter(
            new_file_name,
            cv2.VideoWriter_fourcc(*"mp4v"),
            fps,
            (width, height),
        )

        while capture.isOpened():
            ret, frame = capture.read()
            if not ret:
                break

            blured_frame = self.__detect_and_blur(
                Image.fromarray(frame), blur_percentage
            )
            output.write(np.array(blured_frame))

        output.release()
        capture.release()
        temp_file.close()

        with open(new_file_name, "rb") as f:
            content = f.read()

        os.remove(new_file_name)
        return content

    def __detect_and_blur(self, image: Image, percentage: int) -> Image:
        detections = self.detection_service.detect([image])[0]
        boxes = list(
            map(
                lambda det: tuple(map(lambda coord: int(coord), det.coords)), detections
            )
        )

        return self.images_service.blur_boxes(
            image,
            boxes=boxes,
            percentage=percentage,
        )


converter_service = ConverterService(
    detection_service=detection_service_realization,
    images_service=images_service_realization,
)
