import grpc
import audio_streaming_pb2
import audio_streaming_pb2_grpc

class AudioStreamerClient:
  def __init__(self, server_address):
    self.channel = grpc.insecure_channel(server_address)
    self.stub = audio_streaming_pb2_grpc.AudioStreamerStub(self.channel)

  def stream_audio(self, audio_chunks):
    response_chunks = self.stub.StreamAudio(audio_chunks)
    for response_chunk in response_chunks:
      # Process the response audio chunk here
      # ...
      pass

if __name__ == '__main__':
  client = AudioStreamerClient('localhost:50051')
  with open('audio_file.wav', 'rb') as f:
    while True:
      chunk = f.read(1024)
      if not chunk:
        break
      request_chunk = audio_streaming_pb2.AudioChunk(audio=chunk)
      client.stream_audio([request_chunk])
