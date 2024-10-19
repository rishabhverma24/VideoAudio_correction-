from moviepy.editor import VideoFileClip, AudioFileClip

def overlay_audio(video_filename, audio_filename, output_filename):
    """Remove the original audio from the video and overlay the new audio."""
    # Load the video file
    video = VideoFileClip(video_filename)
    
    # Load the new audio file
    new_audio = AudioFileClip(audio_filename)
    
    # Set the new audio to the video (removing the original audio)
    final_video = video.set_audio(new_audio)
    
    # Write the result to a new video file
    final_video.write_videofile(output_filename, codec='libx264', audio_codec='aac')

if __name__ == "__main__":
    input_video = "input_video.mp4"  # Original video file
    new_audio = "output_audio.mp3"    # New audio file generated from text
    output_video = "output_video.mp4"  # Output video file name

    overlay_audio(input_video, new_audio, output_video)
