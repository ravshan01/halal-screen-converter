# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from halal_screen_proto import converter_service_pb2 as halal__screen__proto_dot_converter__service__pb2


class ConverterServiceStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.Convert = channel.unary_unary(
                '/ConverterService/Convert',
                request_serializer=halal__screen__proto_dot_converter__service__pb2.ConvertRequest.SerializeToString,
                response_deserializer=halal__screen__proto_dot_converter__service__pb2.ConvertResponse.FromString,
                )


class ConverterServiceServicer(object):
    """Missing associated documentation comment in .proto file."""

    def Convert(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_ConverterServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'Convert': grpc.unary_unary_rpc_method_handler(
                    servicer.Convert,
                    request_deserializer=halal__screen__proto_dot_converter__service__pb2.ConvertRequest.FromString,
                    response_serializer=halal__screen__proto_dot_converter__service__pb2.ConvertResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'ConverterService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class ConverterService(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def Convert(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/ConverterService/Convert',
            halal__screen__proto_dot_converter__service__pb2.ConvertRequest.SerializeToString,
            halal__screen__proto_dot_converter__service__pb2.ConvertResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
