import speech_recognition as sr

def transcribe_audio_file(file_path):
    """
    Transcribes the speech from an audio file using Google's Web Speech API.

    Args:
        file_path (str): The path to the audio file.

    Returns:
        str: The transcribed text, or an error message if transcription fails.
    """
    recognizer = sr.Recognizer()

    try:
        with sr.AudioFile(file_path) as source:
            print("Processing audio...")
            audio_data = recognizer.record(source)

        print("Recognizing the text...")
        text = recognizer.recognize_google(
            audio_data,
            language="en-US"
        )
        return f"Decoded Text: {text}"

    except sr.UnknownValueError:
        return "Error: Google Speech Recognition could not understand audio."
    except sr.RequestError as e:
        return f"Error: Could not request results from Google Speech Recognition service; {e}"
    except FileNotFoundError:
        return f"Error: The file '{file_path}' was not found."
    except Exception as e:
        return f"An unexpected error occurred: {e}"

if __name__ == "__main__":
    audio_file_path = "./sample_audio/speech.wav"
    transcription_result = transcribe_audio_file(audio_file_path)
    print(transcription_result)
