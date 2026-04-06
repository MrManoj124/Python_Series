import speech_recognition as sr

r = sr.Recognizer()

mic_index = 1  # try 1, 5, 9, etc.

with sr.Microphone(device_index=mic_index) as source:
    print("Speak...")
    r.adjust_for_ambient_noise(source)
    audio = r.listen(source)

print("Audio captured")