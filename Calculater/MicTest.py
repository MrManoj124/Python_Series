import speech_recognition as sr

record = sr.Recognizer()
with sr.Microphone() as source:
    print("Speak...")
    audio = record.listen(source)

print("Captured audio")