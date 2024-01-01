import numpy

from detection.enums.type import DetectionType
from detection.protocols.part import DetectionPartProtocol
from detection.services.IDetectionService import IDetectionService
from PIL import Image

from detectron2.utils.logger import setup_logger
from detectron2 import model_zoo
from detectron2.engine import DefaultPredictor
from detectron2.config import get_cfg

setup_logger()


class DetectionService(IDetectionService):
    predictor: DefaultPredictor
    person_type = 0

    def __init__(self):
        cfg = get_cfg()
        # add project-specific config (e.g., TensorMask) here if you're not running a model in detectron2's core library
        cfg.merge_from_file(
            model_zoo.get_config_file(
                "COCO-InstanceSegmentation/mask_rcnn_R_50_FPN_3x.yaml"
            )
        )
        cfg.MODEL.ROI_HEADS.SCORE_THRESH_TEST = 0.5  # set threshold for this model
        # Find a model from detectron2's model zoo. You can use the https://dl.fbaipublicfiles... url as well
        cfg.MODEL.WEIGHTS = model_zoo.get_checkpoint_url(
            "COCO-InstanceSegmentation/mask_rcnn_R_50_FPN_3x.yaml"
        )
        cfg.MODEL.DEVICE = "cpu"
        self.predictor = DefaultPredictor(cfg)

    def detect(
        self,
        image: Image,
        min_percentage_probability: int = 50,
    ) -> list[DetectionPartProtocol]:
        image_arr = numpy.array(image)
        outputs = self.predictor(image_arr)

        person_boxes_indexes = []
        for i, detect_class in enumerate(outputs["instances"].pred_classes):
            if detect_class.item() == self.person_type:
                person_boxes_indexes.append(i)

        return list(
            map(
                lambda i: {
                    "name": DetectionType.Person,
                    "score": outputs["instances"].scores[i].item(),
                    "coords": outputs["instances"].pred_boxes[i].tensor.tolist(),
                },
                person_boxes_indexes,
            )
        )


detection_service = DetectionService()
