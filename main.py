from concurrent import futures
from grpc import server as grpc_server

from converter.services.converter import converter_service
from halal_screen_proto.converter_service_pb2_grpc import (
    add_ConverterServiceServicer_to_server,
)

from converter.servicer import ConverterServiceServicer


def serve():
    server = grpc_server(futures.ThreadPoolExecutor(max_workers=10))
    add_ConverterServiceServicer_to_server(
        ConverterServiceServicer(converter_service), server
    )

    server.add_insecure_port("[::]:50051")
    server.start()
    print("Server started")

    server.wait_for_termination()


def main():
    print("Starting server")
    serve()
    print("Server stopped")


if __name__ == "__main__":
    main()
