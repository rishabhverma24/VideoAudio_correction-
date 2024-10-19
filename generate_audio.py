from gtts import gTTS

def generate_audio(text, filename):
    """Generate audio from the provided text and save it as an MP3 file."""
    tts = gTTS(text=text, lang='en')  # Specify the language
    tts.save(filename)  # Save the audio file
    print(f"Audio saved as: {filename}")

if __name__ == "__main__":
    # Load the corrected text from the file
    with open('corrected_text.txt', 'r') as f:
        corrected_text = f.read()

    # Generate audio from the corrected text
    generate_audio(corrected_text, 'output_audio.mp3')
