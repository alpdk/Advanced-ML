import os
import pathlib

from gtts import gTTS
from playsound import playsound

def play_text_to_speech(text, language = 'en'):
    myobj = gTTS(text=text, lang=language, slow=False)

    path_to_proj_dir = pathlib.Path().resolve()
    path_to_mp3_anser = os.path.join(path_to_proj_dir, "answer.mp3")

    myobj.save(path_to_mp3_anser)

    playsound(path_to_mp3_anser)

    os.remove(path_to_mp3_anser)

if __name__ == '__main__':
    play_text_to_speech("aboba")