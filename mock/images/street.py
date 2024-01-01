from pathlib import PurePath

from detection.enums.type import DetectionType
from mock.type import MockResource, MockResourceEnum

resource = MockResource(
    type=MockResourceEnum.Image,
    path=str(PurePath(__file__).parent / "street.jpg"),
    detections={DetectionType.Person: 3},
)
