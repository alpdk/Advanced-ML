import os
import pathlib
import replicate

from gtts import gTTS
from playsound import playsound

os.environ["'REPLICATE_API_TOKEN'"] = os.getenv('REPLICATE_API_TOKEN')


def assistent_speak(text, language="en",
                    reference_voice="https://www.myinstants.com/en/instant/vergil-i-need-more-power-43083/?utm_source=copy&utm_medium=share"):
    output = replicate.run(
        "lucataco/xtts-v2:684bc3855b37866c0c65add2ff39c78f3dea3f4ff103a436465326e0f438d55e",
        input={
            "text": text,
            "speaker": reference_voice,
            "language": language,
            "cleanup_voice": False
        }
    )

    return output


def play_text_to_speech(text, language='en'):
    sound_ref = assistent_speak(text, language)

    playsound(sound_ref)


if __name__ == '__main__':
    play_text_to_speech("I am a son of sparda")
