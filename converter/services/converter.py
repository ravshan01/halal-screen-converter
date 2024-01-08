import io

from PIL import Image

from detection.services.detection import detection_service
from images.services.images import images_service
from .IConverterService import IConverterService


class ConverterService(IConverterService):
    detection_service = detection_service
    images_service = images_service

    def convert_image(self, image: bytes) -> bytes:
        image_pil = Image.open(io.BytesIO(image))

        detections = self.detection_service.detect(image_pil)
        boxes = list(
            map(
                lambda det: tuple(map(lambda coord: int(coord), det.coords)), detections
            )
        )
        blured_image = self.images_service.blur_boxes(
            image_pil,
            boxes=boxes,
            percentage=50,
        )

        byte_io = io.BytesIO()
        blured_image.save(byte_io, format="PNG")  # TODO: get format from image
        return byte_io.getvalue()


converter_service = ConverterService()

#
# Certainly! I can help you with that. To get video frames using OpenCV in Python, you'll need to follow these steps:
#
# Import the necessary libraries: python import cv2
#
# Open the video file using cv2.VideoCapture(): python video = cv2.VideoCapture('path_to_video_file.mp4')
#
# Iterate over the frames using a loop: ```python while video.isOpened(): ret, frame = video.read()
#
# Perform operations on each frame here
# if not ret: break ```
#
# Within the loop, you can perform any desired operations on each frame. For example, you can display each frame using cv2.imshow(): python cv2.imshow('Video', frame)
#
# To exit the loop, press the 'q' key: python if cv2.waitKey(1) & 0xFF == ord('q'): break
#
# Finally, release the video object and destroy any open windows: python video.release() cv2.destroyAllWindows()
#
# That's it! You can modify the code within the loop to perform various operations on each frame, such as saving them as image files, applying image processing techniques, or extracting specific information. Let me know if you need further assistance or have any other questions!
