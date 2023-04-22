import grpc
from concurrent import futures
import time

import audio_streaming_pb2
import audio_streaming_pb2_grpc

class AudioStreamerServicer(audio_streaming_pb2_grpc.AudioStreamerServicer):
  def StreamAudio(self, request_iterator, context):
    for audio_chunk in request_iterator:
      # Process the audio chunk here
      # ...

      # Yield a response audio chunk
      yield audio_streaming_pb2.AudioChunk(audio=audio_chunk.audio)

def serve():
  server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
  audio_streaming_pb2_grpc.add_AudioStreamerServicer_to_server(AudioStreamerServicer(), server)
  server.add_insecure_port('[::]:50051')
  server.start()
  try:
    while True:
      time.sleep(86400)
  except KeyboardInterrupt:
    server.stop(0)

if __name__ == '__main__':
  serve()
