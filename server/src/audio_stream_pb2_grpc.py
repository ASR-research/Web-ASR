# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

import audio_stream_pb2 as audio__stream__pb2
from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2


class AudioStreamerStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.StreamAudio = channel.stream_unary(
                '/audio_stream.AudioStreamer/StreamAudio',
                request_serializer=audio__stream__pb2.AudioChunk.SerializeToString,
                response_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
                )


class AudioStreamerServicer(object):
    """Missing associated documentation comment in .proto file."""

    def StreamAudio(self, request_iterator, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_AudioStreamerServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'StreamAudio': grpc.stream_unary_rpc_method_handler(
                    servicer.StreamAudio,
                    request_deserializer=audio__stream__pb2.AudioChunk.FromString,
                    response_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'audio_stream.AudioStreamer', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class AudioStreamer(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def StreamAudio(request_iterator,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.stream_unary(request_iterator, target, '/audio_stream.AudioStreamer/StreamAudio',
            audio__stream__pb2.AudioChunk.SerializeToString,
            google_dot_protobuf_dot_empty__pb2.Empty.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
