import speech_recognition as sr

def transcribe_audio(audio_file_path):
    # Initialize recognizer
    recognizer = sr.Recognizer()

    # Load the audio file
    with sr.AudioFile(audio_file_path) as source:
        audio = recognizer.record(source)  # Read the entire audio file

    try:
        # Using Google Web Speech API (requires internet, but no API key)
        transcription = recognizer.recognize_google(audio)
        return transcription
    except sr.UnknownValueError:
        return "Google Web Speech could not understand the audio."
    except sr.RequestError as e:
        return f"Could not request results from Google Web Speech; {e}"

if __name__ == "__main__":
    transcription = transcribe_audio("extracted_audio.wav")
    with open("transcription.txt", "w") as f:
        f.write(transcription)
