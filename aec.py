import speech_recognition
import time
import datetime
# import win32gui, win32ui, win32con, win32api
# import pandas as pd
import pyaudio
import spacy
from spacy import displacy
import pickle
import json

r = speech_recognition.Recognizer()
nlp = spacy.load("D:\sttNlp/ner")
results = {'dir':'', 'floor': '', 'bui':'', 'func':''}
resultsArr = []

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


doc=nlp(text)
# displacy.render(doc, style="ent", jupyter=True)
print(doc.ents)
for ent in doc.ents:
    print(ent.label_+' ------> '+ ent.text)
    print(ent.label_)
    if ent.label_ == 'DIRECTION':
        results['dir'] = ent.text
    elif ent.label_ == 'FLOOR':
        results['floor'] = ent.text
    elif ent.label_ == 'BUILDING':
        results['bui'] = ent.text
    elif ent.label_ == 'FUNCTION':
        results['func'] = ent.text


print(results)

with open(r"D:\sttNlp\output.txt", 'w') as output:
    output.write(json.dumps(results))

with open(r"D:\ue4\User_Testing\Output.txt", 'w') as outputToEngine:
    # arrResults = results['dir'] + "," + results['bui'] + "," + results['func']
    # outputToEngine.write(arrResults)
    outputToEngine.write(json.dumps(results))


    