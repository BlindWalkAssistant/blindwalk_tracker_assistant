import pyttsx3
import threading
import queue

engine = pyttsx3.init()

speech_queue = queue.Queue()


def voice_worker():
    while True:
        text = speech_queue.get()
        if text is None:
            break
        engine.say(text)
        engine.runAndWait()
        speech_queue.task_done()


thread = threading.Thread(target=voice_worker, daemon=True)
thread.start()


def speak(text):
    speech_queue.put(text)