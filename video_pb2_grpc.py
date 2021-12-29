# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

import video_pb2 as video__pb2


class videoStub(object):
    """The greeting service definition.
    """

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.Analyse = channel.stream_stream(
                '/video/Analyse',
                request_serializer=video__pb2.MsgRequest.SerializeToString,
                response_deserializer=video__pb2.MsgReply.FromString,
                )


class videoServicer(object):
    """The greeting service definition.
    """

    def Analyse(self, request_iterator, context):
        """Sends a greeting
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_videoServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'Analyse': grpc.stream_stream_rpc_method_handler(
                    servicer.Analyse,
                    request_deserializer=video__pb2.MsgRequest.FromString,
                    response_serializer=video__pb2.MsgReply.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'video', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class video(object):
    """The greeting service definition.
    """

    @staticmethod
    def Analyse(request_iterator,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.stream_stream(request_iterator, target, '/video/Analyse',
            video__pb2.MsgRequest.SerializeToString,
            video__pb2.MsgReply.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
