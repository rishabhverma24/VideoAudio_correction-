import ffmpeg

def extract_audio(video_path, audio_output_path):
    stream = ffmpeg.input(video_path)
    stream = ffmpeg.output(stream, audio_output_path, acodec='pcm_s16le', ac=1, ar='16000')
    ffmpeg.run(stream)

if __name__ == "__main__":
    extract_audio('input_video.mp4', 'extracted_audio.wav')
