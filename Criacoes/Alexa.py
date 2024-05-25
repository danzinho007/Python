import pyttsx3 
engine = pyttsx3.init()
voices = engine.getProperty('voices')
for voice in voices:
    if 'portuguese' in voice.languages:
        engine.setProperty('voice', voice.id)
        break
text ="Testando"
rate = engine.getProperty('rate')
engine.setProperty('rate', rate - 60)
volume = engine.getProperty('volume')
engine.setProperty('volume', volume + 0.25)
engine.say(text)
engine.runAndWait()
