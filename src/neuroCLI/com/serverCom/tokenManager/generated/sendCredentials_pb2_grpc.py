# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""

import grpc
import warnings

from neuroCLI.com.serverCom.tokenManager.generated import (
    sendCredentials_pb2 as sendCredentials__pb2,
)

GRPC_GENERATED_VERSION = "1.69.0"
GRPC_VERSION = grpc.__version__
_version_not_supported = False

try:
    from grpc._utilities import first_version_is_lower

    _version_not_supported = first_version_is_lower(
        GRPC_VERSION, GRPC_GENERATED_VERSION
    )
except ImportError:
    _version_not_supported = True

if _version_not_supported:
    raise RuntimeError(
        f"The grpc package installed is at version {GRPC_VERSION},"
        + f" but the generated code in sendCredentials_pb2_grpc.py depends on"
        + f" grpcio>={GRPC_GENERATED_VERSION}."
        + f" Please upgrade your grpc module to grpcio>={GRPC_GENERATED_VERSION}"
        + f" or downgrade your generated code using grpcio-tools<={GRPC_VERSION}."
    )


class VerifyCredentialsServiceStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.verifyCredentials = channel.unary_unary(
            "/tokenManager.sendCredentials.VerifyCredentialsService/verifyCredentials",
            request_serializer=sendCredentials__pb2.sendCredentials.SerializeToString,
            response_deserializer=sendCredentials__pb2.VerifyCredentialsResponse.FromString,
            _registered_method=True,
        )


class VerifyCredentialsServiceServicer(object):
    """Missing associated documentation comment in .proto file."""

    def verifyCredentials(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details("Method not implemented!")
        raise NotImplementedError("Method not implemented!")


def add_VerifyCredentialsServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
        "verifyCredentials": grpc.unary_unary_rpc_method_handler(
            servicer.verifyCredentials,
            request_deserializer=sendCredentials__pb2.sendCredentials.FromString,
            response_serializer=sendCredentials__pb2.VerifyCredentialsResponse.SerializeToString,
        ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
        "tokenManager.sendCredentials.VerifyCredentialsService", rpc_method_handlers
    )
    server.add_generic_rpc_handlers((generic_handler,))
    server.add_registered_method_handlers(
        "tokenManager.sendCredentials.VerifyCredentialsService", rpc_method_handlers
    )


# This class is part of an EXPERIMENTAL API.
class VerifyCredentialsService(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def verifyCredentials(
        request,
        target,
        options=(),
        channel_credentials=None,
        call_credentials=None,
        insecure=False,
        compression=None,
        wait_for_ready=None,
        timeout=None,
        metadata=None,
    ):
        return grpc.experimental.unary_unary(
            request,
            target,
            "/tokenManager.sendCredentials.VerifyCredentialsService/verifyCredentials",
            sendCredentials__pb2.sendCredentials.SerializeToString,
            sendCredentials__pb2.VerifyCredentialsResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True,
        )