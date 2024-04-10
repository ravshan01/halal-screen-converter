from halal_screen_proto.converter_service_pb2 import (
    ConvertRequest,
    ConvertContentType,
)
from halal_screen_proto.converter_service_pb2_grpc import (
    ConverterServiceServicer as ConverterServiceServicerBase,
)
from converter.services.IConverterService import IConverterService


class ConverterServiceServicer(ConverterServiceServicerBase):
    def __init__(self, converter_service: IConverterService):
        super().__init__()
        self.__converter_service = converter_service

    def Convert(self, request: ConvertRequest, context):
        if request.type == ConvertContentType.IMAGE:
            content = self.__converter_service.convert_image(
                request.content,
                request.blur_percentage,
            )

        elif request.type == ConvertContentType.VIDEO:
            content = self.__converter_service.convert_video(
                request.content,
                request.blur_percentage,
            )

        return ConvertRequest(content=content)
