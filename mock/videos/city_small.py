from pathlib import PurePath

from mock.type import MockResource, MockResourceEnum

resource = MockResource(
    type=MockResourceEnum.Video, path=str(PurePath(__file__).parent / "city-small.mp4")
)
