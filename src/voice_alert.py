import pyttsx3
import threading
import queue
import time

speech_queue = queue.Queue()

def get_best_voice(engine):
    """Try to find a female/clear voice."""
    voices = engine.getProperty('voices')
    for voice in voices:
        name = voice.name.lower()
        if "female" in name or "zira" in name or "hazel" in name:
            return voice.id
    return voices[0].id if voices else None

def voice_worker():
    # Initialize engine inside the thread for better reliability on Windows
    try:
        engine = pyttsx3.init()
        
        # Enhanced voice properties
        engine.setProperty('rate', 155)    # Slightly faster for responsiveness
        engine.setProperty('volume', 0.6)  # Set to 60% as requested
        
        best_voice = get_best_voice(engine)
        if best_voice:
            engine.setProperty('voice', best_voice)
    except Exception as e:
        print(f"Voice Init Error: {e}")
        return

    while True:
        try:
            text = speech_queue.get()
            if text is None:
                break
            
            # Speak only the latest message if multiple are queued
            while not speech_queue.empty():
                text = speech_queue.get_nowait()
                if text is None: return

            engine.say(text)
            engine.runAndWait()
            speech_queue.task_done()
        except Exception as e:
            print(f"Voice Worker Error: {e}")
            time.sleep(0.1)

thread = threading.Thread(target=voice_worker, daemon=True)
thread.start()

def speak(text):
    """Add text to speech queue."""
    speech_queue.put(text)