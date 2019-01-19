import speech_recognition as sr



r = sr.Recognizer()
with sr.Microphone() as source:
    print("Record your voice:")
    audio = r.listen(source)
    try:
        text = r.recognize_google(audio)
        print("You said : {}".format(text))
    except:
        print("I am afraid I don't understand")
