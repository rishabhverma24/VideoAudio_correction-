import os
from extract_audio import extract_audio
from transcribe_audio import transcribe_audio
from correct_transcription import correct_transcription
from generate_audio import generate_audio
from sync_audio_video import overlay_audio

if __name__ == "__main__":
    video_file = 'input_video.mp4'
    
    # Step 1: Extract Audio
    extract_audio(video_file, 'extracted_audio.wav')
    
    # Step 2: Transcribe Audio
    transcription = transcribe_audio('extracted_audio.wav')
    with open('transcription.txt', 'w') as f:
        f.write(transcription)

    # Step 3: Correct Transcription
    corrected_text = correct_transcription(transcription)
    with open('corrected_text.txt', 'w') as f:
        f.write(corrected_text)

    # Step 4: Convert Corrected Text to Speech
    generate_audio(corrected_text, 'output_audio.mp3')

    # Step 5: Sync Audio with Video
    overlay_audio(video_file, 'output_audio.mp3', 'output_video.mp4')
