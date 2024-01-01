import numpy

from detection.enums.type import DetectionType
from detection.dataclasses.part import DetectionPart
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
        # TODO: check support cuda and use it
        cfg.MODEL.DEVICE = "cpu"
        self.predictor = DefaultPredictor(cfg)

    def detect(
        self,
        image: Image,
        min_percentage_probability: int = 50,
    ) -> list[DetectionPart]:
        outputs = self.predictor(numpy.array(image))
        person_instances = outputs["instances"][
            outputs["instances"].pred_classes == self.person_type
        ]

        return list(
            map(
                lambda i: DetectionPart(
                    name=DetectionType.Person,
                    score=person_instances.scores[i].item(),
                    coords=tuple(*person_instances.pred_boxes[i].tensor.tolist()),
                ),
                range(len(person_instances)),
            )
        )


detection_service = DetectionService()
