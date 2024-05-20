import speech_recognition as sr
import pyttsx3
import sounddevice

r = sr.Recognizer()

def record_text():
    while True:
        try:
            with sr.Microphone() as source:

                r.adjust_for_ambient_noise(source, duration=0.2)

                audio = r.listen(source, 30, 10)

                MyText = r.recognize_google(audio)

                return MyText

        except sr.RequestError as e:
            print(f"Could not request results: {e}")
        except sr.UnknownValueError:
            print("Unknown value occurred")
            return ""

def output_text(text):
    f = open("output.txt", "a")
    f.write(text)

    f.write('\n')

    f.close()

    return

if __name__ == '__main__':
    while True:
        text = record_text()

        print(f"Pronounced text: '{text}'.")