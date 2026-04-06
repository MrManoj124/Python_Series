#import speech_recognition as sr
import speech_recognition as sr

#print(sr.Microphone.list_microphone_names())

record = sr.Recognizer()
with sr.Microphone() as source:
    print("Speak...")
    audio = record.listen(source)

print("Captured audio")