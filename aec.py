import speech_recognition
import time
import datetime
import win32gui, win32ui, win32con, win32api
import pandas as pd
import spacy
from spacy import displacy
import pickle

r = speech_recognition.Recognizer()
nlp = spacy.load("ner")

with  speech_recognition.Microphone() as source:
    print('Speak Anything: ')
    audio = r.listen(source)
    try:
        text = r.recognize_google(audio, language='en-US')
        print('You said : {}'.format(text))
    except:
        print('Sorry, could not recognize your voice')

f=open(r"D:\sttNlp\results.txt","w")
f.write(text)
f.close()
print(text)

doc=nlp(text)
displacy.render(doc, style="ent", jupyter=True)
print(doc.ents)
