from gtts import gTTS

#pip install gtts

from playsound import playsound

# pip install playsound

audio = 'speech.mp3'

Language = 'en'
text = input("Enter Text here... : ")
sp = gTTS(text, lang language, slow=False)

sp.save(audio) playsound(audio)