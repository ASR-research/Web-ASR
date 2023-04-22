import grpc
import audio_stream_pb2
import audio_stream_pb2_grpc
from concurrent import futures

class AudioStreamServicer(audio_stream_pb2_grpc.AudioStreamerServicer):
    def StreamAudio(self, request_iterator, context):
        for audio_request in request_iterator:
            # Do something with the audio data
            audio_chunk = audio_request.audio_chunk
            print(f"Received {len(audio_chunk)} bytes of audio data")
            # Send the audio data back to the client
            audio_response = audio_stream_pb2.AudioChunk()
            audio_response.audio_chunk = audio_chunk
            yield audio_response

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    audio_stream_pb2_grpc.add_AudioStreamerServicer_to_server(AudioStreamServicer(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    print("Server started and listening on port 50051...")
    server.wait_for_termination()

if __name__ == '__main__':
    serve()
