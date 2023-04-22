import grpc
import audio_stream_pb2
import audio_stream_pb2_grpc
import pyaudio

def audio_generator(audio_file):
    chunk_size = 1024
    with open(audio_file, 'rb') as f:
        while True:
            audio_chunk = f.read(chunk_size)
            if not audio_chunk:
                break
            audio_request = audio_stream_pb2.AudioChunk/()
            audio_request.audio_chunk = audio_chunk
            yield audio_request

def stream_audio(stub, audio_file):
    response_iterator = stub.StreamAudio(audio_generator(audio_file))
    for audio_response in response_iterator:
        # Do something with the audio data
        audio_chunk = audio_response.audio_chunk
        print(f"Received {len(audio_chunk)} bytes of audio data")

def main():
    channel = grpc.insecure_channel('localhost:50051')
    stub = audio_stream_pb2_grpc.AudioStreamerStub(channel)
    audio_file = 'audio.wav'
    stream_audio(stub, audio_file)

if __name__ == '__main__':
    main()
