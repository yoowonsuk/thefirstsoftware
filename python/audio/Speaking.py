import pyttsx3

engine_object = pyttsx3.init()
engine_object.setProperty('rate', 200)
engine_object.setProperty('voice', 'f1') # f1 ~ f12
engine_object.say("hello world")

engine_object.runAndWait()

