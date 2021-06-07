import wx
import playsound
from gtts import gTTS
import os
import random
import speech_recognition as sr
from GUI import *
class Main:
    def __init__(self):
        self.r = sr.Recognizer()
        self.mic = sr.Microphone()
    
    def listen(self):
        with self.mic as source:
            self.read("Speak something")
            self.audio = self.r.listen(source)
            try:
                text = self.r.recognize_google(self.audio)
                print("You said : {}".format(text))
            except:
                self.read("Your audio input was not detected")

    def read(self):
        myobj = gTTS(text=self.audio, lang="en", slow=False)
        rand = random.randint(1,20000000)
        audio_file = 'audio' + str(rand) + '.mp3'
        myobj.save(audio_file)
        playsound.playsound(audio_file)
        os.remove(audio_file)

def main():
    app = wx.App()
    WindowClass(None, title='Edith')
    app.MainLoop()
main()
