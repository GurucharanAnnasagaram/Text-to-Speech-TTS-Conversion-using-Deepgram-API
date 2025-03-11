import os
from dotenv import load_dotenv

load_dotenv()
from deepgram import DeepgramClient, SpeakOptions

filename = "speech.wav"


def text2speech(text_input):
    try:
        SPEAK_OPTIONS = {"text": text_input}
        deepgram = DeepgramClient(api_key=os.getenv("DQ_API_KEY"))
        options = SpeakOptions(
            model="aura-asteria-en",
            encoding="linear16",
            container="wav"
        )
        response = deepgram.speak.v("1").save(filename, SPEAK_OPTIONS, options)
        return filename
    except Exception as e:
        print(f"Exception : {e}")


if __name__ == "__main__":
    text2speech("This is sparta")
